import threading

import cv2

from inside_classes import logic
from inside_classes import pre_process_data
from inside_classes import process_data
from inside_classes import tracker


class processor:
    cap = None
    defaultFrame = None
    main_thread = None
    pre_process_obj = None
    tracker_obj = None
    process_data_obj = None
    logic_and_output_obj = None
    def __del__(self):
        self.main_thread.join()
    def __init__(self, cap='deafault'):
        if (cap != 'deafault'):
            self.cap = cap
        self.cap = cv2.VideoCapture(r"C:\Users\vwork\PycharmProjects\droneDetector_V1\dataset\drone_vid_2.mp4")
        self.read_frame()
        self.pre_process_obj = pre_process_data.pre_process_data()
        self.tracker_obj = process_data.process_data()
        self.process_data_obj = tracker.tracker_mgmt()
        self.logic_and_output_obj = logic.logic(self.tracker_obj, self.process_data_obj)

        self.main_thread = threading.Thread(target=self.run)
        self.main_thread.start()

    def read_frame(self):
        ok, self.defaultFrame = self.cap.read()
        if (not ok):
            raise "frames_end"
    def show(self):
        cv2.imshow('procesor_default_frame', self.defaultFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

    def run(self):
        while True:
            cv2.imshow('procesor_default_frame', self.defaultFrame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            self.read_frame()
            self.pre_process_obj.proc(self.defaultFrame)
            if (type(self.pre_process_obj.processed_frame )!=None):
                self.tracker_obj.filters_1(self.pre_process_obj.processed_frame)
                self.process_data_obj.proc(self.pre_process_obj.processed_frame)
            self.logic_and_output_obj.do_sth()
