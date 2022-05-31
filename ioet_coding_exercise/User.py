from ioet_coding_exercise.WorkStatement import WorkStatement


class User:
    """
    Users in the systemm, in this particular case is the same as a employee

    Attributes:
        name {str}: User's name.
        statements {list}: List of WorkStatements. All worked entries recorded
            for the user.
    """

    def __init__(self, name: str, statements: list[WorkStatement] = None):
        self.name = name
        self.statements = statements or []
