import enum
class pre_process_data:
    default_frame=None
    processed_frame=None

    def show(self):
        None
    def proc(self,frame='default'):
        if(type(frame)!=type('default')):
            self.default_frame = frame
        #process frame
        self.processed_frame=frame
        return self.processed_frame

    class settings_to_pre_frame(enum.Enum):
        width=0
        heigth=0
