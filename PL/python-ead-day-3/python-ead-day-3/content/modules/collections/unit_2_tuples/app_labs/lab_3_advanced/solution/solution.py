"""
Lab 3 (Advanced): Vital Signs Monitor - Part 3
Solution Code

Module: Collections - Unit 2: Tuples
"""
from collections import namedtuple

Reading = namedtuple("Reading", ["time", "hr", "temp"])

def convert_to_namedtuples(raw_data):
    """Convert list of (time, hr, temp) to Reading objects."""
    # List comprehension unpacking arguments
    return [Reading(*row) for row in raw_data]


def analyze_overall_trend(readings):
    """Calculate change from start to end."""
    if not readings:
        return (0, 0)
    first = readings[0]
    last = readings[-1]
    return (last.hr - first.hr, last.temp - first.temp)


def find_rapid_changes(readings):
    """Find instances where HR changed > 20 between consecutive readings."""
    changes = []
    # Use zip to pair (i, i+1)
    for prev, curr in zip(readings[:-1], readings[1:]):
        delta = curr.hr - prev.hr
        if abs(delta) > 20:
            changes.append((curr.time, delta))
    return changes
