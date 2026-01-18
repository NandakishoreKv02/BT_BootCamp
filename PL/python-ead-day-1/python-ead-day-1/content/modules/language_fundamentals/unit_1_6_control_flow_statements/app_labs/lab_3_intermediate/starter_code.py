"""
Lab 3: Vital Sign Monitor - Starter Code
"""

def poll_until_stable(readings):
    """
    Search for a heart rate reading in the stable range [60, 100].
    
    Args:
        readings (list): List of integers.
        
    Returns:
        int or None: The first reading in range, or None.
    """
    # TODO: Implement while loop logic
    i = 0
    while i < len(readings) and (readings[i] < 60 or readings[i] > 100):
        i += 1
    
    if i < len(readings):
        return readings[i]
    return None

if __name__ == "__main__":
    vitals = [150, 120, 110, 85, 75, 70]
    print(f"First stable reading: {poll_until_stable(vitals)}")
    
    unstable = [150, 160, 170]
    print(f"No stable reading: {poll_until_stable(unstable)}")
