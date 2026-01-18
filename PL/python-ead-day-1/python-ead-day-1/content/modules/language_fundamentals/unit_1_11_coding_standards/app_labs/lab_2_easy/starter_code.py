"""
Lab 2: The Magic Number Mirror - Starter Code
"""

MIN_NORMAL_HR = 60
MAX_NORMAL_HR = 100

def check_vital_alert(heart_rate):
    """
    Check if the heart rate is within normal bounds.
    """
    if heart_rate < MIN_NORMAL_HR or heart_rate > MAX_NORMAL_HR:
        return "ALERT"
    return "NORMAL"

if __name__ == "__main__":
    print(f"60 BPM: {check_vital_alert(60)}")
    print(f"110 BPM: {check_vital_alert(110)}")
