class Printer:
    def __init__(self, format: str):
        self._format = format

    def write(self, kwargs):
        print(self._format.format(**kwargs))
