from datetime import timedelta

from ioet_coding_exercise.Payout import Payout
from ioet_coding_exercise.User import User
from ioet_coding_exercise.WorkStatement import WorkStatement


def test_payout():
    users = []

    new_user = User(name="Ariel")
    new_user.statements = [
        WorkStatement(
            day="MO",
            start_time=timedelta(hours=8, minutes=00),
            end_time=timedelta(hours=11, minutes=00),
        )
    ]

    users.append(new_user)

    payouts = Payout.run(users=users)

    assert type(payouts) is list
    assert len(payouts) == 1
    assert payouts[0]["username"] == "Ariel"
    assert payouts[0]["salary"] == 55.0
