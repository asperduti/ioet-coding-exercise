from datetime import timedelta
from ioet_coding_exercise.WorkStatement import WorkStatement


def test_work_statement():
    work_statement = WorkStatement(day="MO", start_time="10:00", end_time="11:00")

    assert work_statement.day == "MO"
    assert work_statement.start_time == timedelta(hours=10, minutes=00)
    assert work_statement.end_time == timedelta(hours=11, minutes=00)


def test_work_statement_get_cost():
    work_statement = WorkStatement(day="MO", start_time="10:00", end_time="11:00")

    assert work_statement.get_cost() == 15.0


def test_work_statement_get_cost_multiple_rules():
    work_statement = WorkStatement(day="MO", start_time="8:00", end_time="11:00")

    assert work_statement.get_cost() == 55.0
