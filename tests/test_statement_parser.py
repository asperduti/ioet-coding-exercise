from ioet_coding_exercise.StatementParser import StatementParser
from ioet_coding_exercise.User import User


def test_statementparser():
    statement = "RENE=MO10:00-12:00,TU10:00-12:00"

    statement_parsed = StatementParser.parse(statement)

    assert type(statement_parsed) is User
    assert statement_parsed.name == "RENE"
    assert type(statement_parsed.statements) is list
    assert len(statement_parsed.statements) == 2
