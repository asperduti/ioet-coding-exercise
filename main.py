from ioet_coding_exercise.FileDataLoader import FileDataLoader
from ioet_coding_exercise.Printer import Printer
from ioet_coding_exercise.Payout import Payout


def main():
    db = FileDataLoader("registros.txt")
    output = Printer("The amount to pay {username} is: {payout} USD")

    payouts = Payout.run(users=db.get_users())
    for payout in payouts:
        output.write({"username": payout["username"], "payout": payout["salary"]})


if __name__ == "__main__":
    main()
