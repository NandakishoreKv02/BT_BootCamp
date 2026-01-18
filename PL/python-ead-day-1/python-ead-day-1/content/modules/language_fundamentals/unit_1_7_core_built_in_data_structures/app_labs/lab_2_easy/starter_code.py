"""
Lab 2: Clinical Reference Ranges - Starter Code
"""

def get_hr_range():
    """Return the normal heart rate range as a tuple."""
    return (60, 100)

def is_value_normal(value, reference_tuple):
    """Unpack ref tuple and check if value is in range."""
    min_val, max_val = reference_tuple
    return min_val <= value <= max_val

if __name__ == "__main__":
    ref = get_hr_range()
    print(f"Is 80 normal? {is_value_normal(80, ref)}")
    print(f"Is 110 normal? {is_value_normal(110, ref)}")
