from ioet_coding_exercise.User import User


class Payout:
    """
    Compute the payments for each user.
    """

    @staticmethod
    def run(users: list[User]) -> list:
        payouts = []

        for user in users:
            salary = 0.0
            for work_statement in user.statements:
                salary += work_statement.get_cost()

            payouts.append({"username": user.name, "salary": salary})

        return payouts
