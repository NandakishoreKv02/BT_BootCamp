"""
Lab 3: Multi-Vital Alert System - Starter Code
"""

def should_trigger_critical_alert(temp, spo2, is_conscious):
    """
    Determine if a patient is at critical risk.
    
    Args:
        temp (float): Body temperature.
        spo2 (int): Oxygen saturation.
        is_conscious (bool): State of consciousness.
        
    Returns:
        bool: True if alert needed, False otherwise.
    """
    return (temp > 39.0 and spo2 < 92) or not is_conscious

if __name__ == "__main__":
    print(f"High risk (39.5C, 90%, True): {should_trigger_critical_alert(39.5, 90, True)}")
