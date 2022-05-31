from ioet_coding_exercise.Payout import Payout
from ioet_coding_exercise.FileDataLoader import FileDataLoader
from ioet_coding_exercise.StatementParser import StatementParser


def test_payout():
    loader = FileDataLoader("registros.txt")
    parser = StatementParser()

    Payout.run(data=loader, parser=parser)

    assert True
