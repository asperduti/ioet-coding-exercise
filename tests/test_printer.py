from io import StringIO
from ioet_coding_exercise.Printer import Printer

import sys


def test_printer():
    printer = Printer("{user} payout {payout}")

    out = StringIO()
    sys.stdout = out
    printer.write({"user": "Ariel", "payout": 2})
    sys.stdout = sys.__stdout__
    output = out.getvalue().strip()
    assert output == "Ariel payout 2"
