class User:
    def __init__(self, name, statements: list = None):
        self.name = name
        self.statements = statements if statements is not None else []
