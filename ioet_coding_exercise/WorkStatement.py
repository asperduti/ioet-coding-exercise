from ioet_coding_exercise.Rules import DAYS_RATES
from ioet_coding_exercise.utils import str_to_time


class WorkStatement:
    def __init__(self, day: str, start_time: str, end_time: str):
        self.day = day
        self.start_time = str_to_time(start_time)
        self.end_time = str_to_time(end_time)

    def get_cost(self) -> float:
        day_rules = DAYS_RATES[self.day]
        cost = 0
        aux_start_time = self.start_time

        for rule in day_rules:
            if rule["START_TIME"] <= aux_start_time <= rule["END_TIME"]:
                if self.end_time <= rule["END_TIME"]:
                    hours = self.end_time - aux_start_time
                else:
                    hours = rule["END_TIME"] - aux_start_time
                    aux_start_time = rule["END_TIME"]

                cost += hours.total_seconds() * rule["RATE"] / 3600
        return cost
