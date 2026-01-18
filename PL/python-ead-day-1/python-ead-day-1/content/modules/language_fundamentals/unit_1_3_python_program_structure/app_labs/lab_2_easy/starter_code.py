"""
Lab 2: Vital Signs Validator - Starter Code
"""

SPO2_CRITICAL = 90
SPO2_WARNING = 95
HR_CRITICAL_THRESHOLD = 120
HR_WARNING_THRESHOLD = 100


def check_vitals(heart_rate, spo2):
    """
    Check patient vitals and determine triage status.

    Args:
        heart_rate (int): Patient's heart rate in BPM.
        spo2 (int): Patient's oxygen saturation (0-100).

    Returns:
        str: 'Critical', 'Warning', 'Stable', or 'Invalid Input'
    """
    if spo2 < 0 or spo2 > 100 or heart_rate < 0:
        return "Invalid Input"
    
    if spo2 < SPO2_CRITICAL or (heart_rate > HR_CRITICAL_THRESHOLD and spo2 < SPO2_WARNING):
        return "Critical"
    
    if spo2 < SPO2_WARNING or heart_rate > HR_WARNING_THRESHOLD:
        return "Warning"
    
    return "Stable"


if __name__ == "__main__":
    print(check_vitals(80, 98))
    print(check_vitals(121, 94))
    print(check_vitals(110, 98))
