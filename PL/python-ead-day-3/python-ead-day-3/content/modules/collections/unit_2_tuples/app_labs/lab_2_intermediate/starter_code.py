"""
Lab 2 (Intermediate): Vital Signs Monitor - Part 2
Starter Code

Module: Collections - Unit 2: Tuples
"""

def calculate_average_hr(readings):
    """
    Calculate average heart rate from readings.
    Each reading is (time, hr, temp).
    
    Returns:
        float: Average HR
    """
    # TODO: Iterate and sum HR
    pass


def find_fever_incidents(readings):
    """
    Find timestamps where temp > 38.0.
    
    Returns:
        list: List of timestamp strings
    """
    # TODO: Filter readings
    pass


def generate_summary(readings):
    """
    Generate daily summary.
    
    Returns:
        tuple: (min_hr, max_hr, avg_temp)
    """
    # TODO: Calculate aggregations and return tuple
    pass


# ==========================
# Manual Testing
# ==========================

if __name__ == "__main__":
    print("="*60)
    print("Lab 2 (Intermediate): Vitals Analyzer")
    print("="*60)
    
    data = [
        ("08:00", 72, 36.6),
        ("12:00", 110, 39.5), # High HR, High Temp
        ("16:00", 65, 36.5)
    ]
    
    avg = calculate_average_hr(data)
    print(f"Avg HR: {avg} (Expected ~82.3)")
    
    fever = find_fever_incidents(data)
    print(f"Fever Times: {fever}")
    
    summary = generate_summary(data)
    print(f"Summary (MinHR, MaxHR, AvgTemp): {summary}")
