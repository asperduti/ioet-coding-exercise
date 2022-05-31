class FileDataLoader:
    """
    Open a file.

    Attributes:
        filepath {str}: The full path of the file to open.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_data(self):
        return open(self.filepath)
