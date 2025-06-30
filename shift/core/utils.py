from datetime import datetime, timedelta


def time_year():
    """Метод для получения даты через год от текущей даты."""

    time = datetime.now()
    year = timedelta(days=365)
    new_date = time + year
    return new_date
