from io import TextIOWrapper
from ioet_coding_exercise.FileDataLoader import FileDataLoader


def test_file_data_loader():
    file_loader = FileDataLoader(filepath="registros.txt")

    assert type(file_loader.get_data()) is TextIOWrapper
