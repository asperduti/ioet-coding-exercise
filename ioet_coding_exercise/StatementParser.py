class StatementParser:
    @classmethod
    def parse(self, statement: str) -> dict:
        result = {}
        user, work_statements = statement.strip().split("=")
        result["user"] = user
        result["work_statements"] = []
        for work_statement in work_statements.split(","):
            day = work_statement[:2]
            times = work_statement[2:]
            start_time, end_time = times.split("-")

            result["work_statements"].append(
                {
                    "day": day,
                    "start_time": start_time,
                    "end_time": end_time,
                }
            )
        return result
