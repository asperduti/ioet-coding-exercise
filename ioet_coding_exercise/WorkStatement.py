from datetime import timedelta
from ioet_coding_exercise.Rules import DAYS_RATES


class WorkStatement:
    """
    A WorkStatement is an statement or entry of the worked hours in a day.

    Attributes:
        day {str}: The initials of the day. According to the bussines logic it
            can be one of the follorings: MO=Monday, TU=Tuesday, WE=Wednesday,
            TH=Thursday, FR=Friday, SA=Saturday, SU=Sunday
        start_time {timedelta}: The time at which the user started to work,
            given by HH:MM.
        end_time {timedelta}: The time at which the user ended to work,
            given by HH:MM.
    """

    def __init__(self, day: str, start_time: timedelta, end_time: timedelta):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    def get_cost(self) -> float:
        """Return the cost of the Work Statement.

        Computes the cost of the Work Statement, taking into account the
        number of hours worked and the rate to apply according to the day and
        time.
        Handles the case where the user may be working at more than one hourly
        rate for the same day.
        """
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
