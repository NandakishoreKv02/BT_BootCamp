"""
Lab 2 (Intermediate): Vital Signs Monitor - Part 2
Solution Code

Module: Collections - Unit 2: Tuples
"""

def calculate_average_hr(readings):
    """Calculate average heart rate."""
    if not readings:
        return 0
    
    total_hr = 0
    for time, hr, temp in readings:
        total_hr += hr
        
    return total_hr / len(readings)


def find_fever_incidents(readings):
    """Find timestamps where temp > 38.0."""
    fevers = []
    for time, hr, temp in readings:
        if temp > 38.0:
            fevers.append(time)
    return fevers


def generate_summary(readings):
    """Generate daily summary (min_hr, max_hr, avg_temp)."""
    if not readings:
        return (0, 0, 0)
        
    hrs = [r[1] for r in readings] # Could iterate manually too
    temps = [r[2] for r in readings]
    
    min_hr = min(hrs)
    max_hr = max(hrs)
    avg_temp = sum(temps) / len(temps)
    
    return (min_hr, max_hr, avg_temp)
