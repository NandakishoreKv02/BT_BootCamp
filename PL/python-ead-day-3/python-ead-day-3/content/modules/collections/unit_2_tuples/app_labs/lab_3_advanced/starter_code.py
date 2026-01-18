"""
Lab 3 (Advanced): Vital Signs Monitor - Part 3
Starter Code

Module: Collections - Unit 2: Tuples
"""
from collections import namedtuple

# Define globally available for tests
Reading = namedtuple("Reading", ["time", "hr", "temp"])

def convert_to_namedtuples(raw_data):
    """
    Convert list of (time, hr, temp) to Reading objects.
    
    Returns:
        list: List of Reading namedtuples
    """
    # TODO: List comprehension to create Readings
    pass


def analyze_overall_trend(readings):
    """
    Calculate change from start to end.
    
    Returns:
        tuple: (hr_delta, temp_delta)
    """
    # TODO: Subtract first from last
    pass


def find_rapid_changes(readings):
    """
    Find instances where HR changed > 20 between consecutive readings.
    
    Returns:
        list: List of (time, change_amount) tuples
    """
    # TODO: Compare current vs previous
    pass


# ==========================
# Manual Testing
# ==========================

if __name__ == "__main__":
    print("="*60)
    print("Lab 3 (Advanced): Vital Trends")
    print("="*60)
    
    raw = [
        ("08:00", 70, 36.5),
        ("09:00", 72, 36.6),
        ("10:00", 95, 36.7) # Spike of +23
    ]
    
    print(f"Raw: {raw}")
    
    # Convert
    nt_list = convert_to_namedtuples(raw)
    print(f"NamedTuples: {nt_list}")
    print(f"Accessing first HR via name: {nt_list[0].hr}")
    
    # Trends
    trend = analyze_overall_trend(nt_list)
    print(f"Overall Trend (Start -> End): {trend}")
    
    # Rapid Change
    spikes = find_rapid_changes(nt_list)
    print(f"Rapid Changes: {spikes}")
