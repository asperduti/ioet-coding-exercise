from ioet_coding_exercise.User import User
from ioet_coding_exercise.StatementParser import StatementParser


class FileDataLoader:
    """
    Open a file.

    Attributes:
        filepath {str}: The full path of the file to open.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.__parser = StatementParser()

    def __get_data(self):
        return open(self.filepath)

    def get_users(self) -> list[User]:
        users: list[User] = []
        for registro in self.__get_data():
            new_user = self.__parser.parse(registro)
            users.append(new_user)

        return users
