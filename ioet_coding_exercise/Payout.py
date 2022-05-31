from ioet_coding_exercise.WorkStatement import WorkStatement
from ioet_coding_exercise.User import User


class Payout:
    """
    Compute the payments for each user.
    """

    @staticmethod
    def run(data, parser):
        for registro in data.get_data():
            registro_parsed = parser.parse(registro)
            work_statements = [
                WorkStatement(
                    day=work_statement["day"],
                    start_time=work_statement["start_time"],
                    end_time=work_statement["end_time"],
                )
                for work_statement in registro_parsed["work_statements"]
            ]

            new_user = User(name=registro_parsed["user"], statements=work_statements)

            salary = 0.0
            for work_statement in new_user.statements:
                salary += work_statement.get_cost()
            print(f"The amount to pay {new_user.name} is: {salary} USD")
