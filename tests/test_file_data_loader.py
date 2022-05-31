from io import TextIOWrapper
from ioet_coding_exercise.FileDataLoader import FileDataLoader


def test_file_data_loader():
    file_loader = FileDataLoader(filepath="examples/registros.txt")

    assert type(file_loader._FileDataLoader__get_data()) is TextIOWrapper


def test_file_data_loader_get_users():
    file_loader = FileDataLoader(filepath="examples/registros.txt")

    assert type(file_loader.get_users()) is list
    assert len(file_loader.get_users()) == 3
