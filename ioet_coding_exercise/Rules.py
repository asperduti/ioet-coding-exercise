from datetime import timedelta

WEEK_RATES = [
    {
        "START_TIME": timedelta(hours=0, minutes=0),
        "END_TIME": timedelta(hours=9, minutes=0),
        "RATE": 25,
    },
    {
        "START_TIME": timedelta(hours=9, minutes=0),
        "END_TIME": timedelta(hours=18, minutes=0),
        "RATE": 15,
    },
    {
        "START_TIME": timedelta(hours=18, minutes=0),
        "END_TIME": timedelta(hours=24, minutes=0),
        "RATE": 20,
    },
]

WEEKEND_RATES = [
    {
        "START_TIME": timedelta(hours=0, minutes=0),
        "END_TIME": timedelta(hours=9, minutes=0),
        "RATE": 30,
    },
    {
        "START_TIME": timedelta(hours=9, minutes=0),
        "END_TIME": timedelta(hours=18, minutes=0),
        "RATE": 20,
    },
    {
        "START_TIME": timedelta(hours=18, minutes=0),
        "END_TIME": timedelta(hours=24, minutes=0),
        "RATE": 25,
    },
]

DAYS_RATES = {
    "MO": WEEK_RATES,
    "TU": WEEK_RATES,
    "WE": WEEK_RATES,
    "TH": WEEK_RATES,
    "FR": WEEK_RATES,
    "SA": WEEKEND_RATES,
    "SU": WEEKEND_RATES,
}
