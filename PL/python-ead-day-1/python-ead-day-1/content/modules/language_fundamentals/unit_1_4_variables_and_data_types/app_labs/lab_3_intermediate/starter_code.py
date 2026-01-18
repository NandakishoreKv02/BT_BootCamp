"""
Lab 3: Clinical Thresholds - Starter Code
"""

FEVER_THRESHOLD = 38.0
HYPERTENSION_SYSTOLIC = 140
HYPERTENSION_DIASTOLIC = 90


def is_fever(temp_celsius):
    """
    Check if patient has fever.
    """
    return temp_celsius >= FEVER_THRESHOLD

def is_hypertensive(systolic, diastolic):
    """
    Check if patient has high blood pressure.
    """
    return systolic >= HYPERTENSION_SYSTOLIC or diastolic >= HYPERTENSION_DIASTOLIC

if __name__ == "__main__":
    print(is_fever(38.5))
