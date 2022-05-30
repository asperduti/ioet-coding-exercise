from datetime import timedelta


def str_to_time(time: str) -> timedelta:
    hours, minutes = time.split(":")
    return timedelta(hours=int(hours), minutes=int(minutes))
