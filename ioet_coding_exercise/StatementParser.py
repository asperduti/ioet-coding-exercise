from ioet_coding_exercise.User import User
from ioet_coding_exercise.WorkStatement import WorkStatement
from ioet_coding_exercise.utils import str_to_time


class StatementParser:
    @classmethod
    def parse(self, statement: str) -> User:

        user, work_statements = statement.strip().split("=")

        new_user = User(name=user)
        work_statements_aux: list[WorkStatement] = []

        for work_statement in work_statements.split(","):
            day = work_statement[:2]
            times = work_statement[2:]
            start_time, end_time = times.split("-")

            new_work_statement = WorkStatement(
                day=day,
                start_time=str_to_time(start_time),
                end_time=str_to_time(end_time),
            )

            work_statements_aux.append(new_work_statement)
        new_user.statements = work_statements_aux

        return new_user
