import sys

from ioet_coding_exercise.FileDataLoader import FileDataLoader
from ioet_coding_exercise.Printer import Printer
from ioet_coding_exercise.Payout import Payout


def main(filepath: str):
    db = FileDataLoader(filepath)
    output = Printer("The amount to pay {username} is: {payout} USD")

    payouts = Payout.run(users=db.get_users())
    for payout in payouts:
        output.write({"username": payout["username"], "payout": payout["salary"]})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide only the filename as argument.")
    else:
        filepath = sys.argv[1]
        main(filepath)
