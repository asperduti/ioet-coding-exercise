from datetime import timedelta


def str_to_time(time: str) -> timedelta:
    """
    Returns the timedelta object for the time in the format string as HH:MM
    """
    hours, minutes = time.split(":")
    return timedelta(hours=int(hours), minutes=int(minutes))
