class prepare_data_class:
    data=None
    def put_data(self, *args):
        self.data=args

    def process_data(self):
        None

    def get_processed_data(self):
        return self.data

