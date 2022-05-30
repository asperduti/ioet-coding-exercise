class FileDataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_data(self):
        return open(self.filepath)
