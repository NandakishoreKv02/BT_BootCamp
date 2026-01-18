"""
Medication Scheduler - Calculate next medication dose times.
"""

from datetime import datetime, timedelta


def parse_time(time_str):
    """
    Parse time string to datetime object.
    
    Args:
        time_str (str): Time in "HH:MM" format.
    
    Returns:
        datetime: Datetime object with today's date.
    """
    return datetime.strptime(time_str, "%H:%M")


def calculate_next_dose(last_dose_time, interval_hours):
    """
    Calculate next medication dose time.
    
    Args:
        last_dose_time (str): Last dose time in "HH:MM" format.
        interval_hours (int): Hours between doses.
    
    Returns:
        str: Next dose time, with (+1 day) if crosses midnight.
    """
    last_time = parse_time(last_dose_time)
    next_time = last_time + timedelta(hours=interval_hours)
    
    if next_time.day > last_time.day:
        return next_time.strftime("%H:%M") + " (+1 day)"
    return next_time.strftime("%H:%M")


if __name__ == "__main__":
    print(calculate_next_dose("08:00", 4))
    print(calculate_next_dose("22:00", 4))
