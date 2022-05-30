from ioet_coding_exercise.StatementParser import StatementParser


def test_statementparser():
    statement = "RENE=MO10:00-12:00,TU10:00-12:00"

    statement_parsed = StatementParser.parse(statement)

    assert type(statement_parsed) is dict
    assert "user" in statement_parsed
    assert "work_statements" in statement_parsed
    assert type(statement_parsed["work_statements"]) is list
    assert len(statement_parsed["work_statements"]) == 2
