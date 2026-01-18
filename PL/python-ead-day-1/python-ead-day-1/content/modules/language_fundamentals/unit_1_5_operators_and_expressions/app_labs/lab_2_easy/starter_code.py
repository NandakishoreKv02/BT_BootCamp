"""
Lab 2: Triage Alert Logic - Starter Code
"""

def is_alert_triggered(heart_rate):
    """
    Check if a heart rate requires an alert.
    
    Args:
        heart_rate (int): Patient heart rate.
        
    Returns:
        bool: True if alert triggered, False otherwise.
    """
    return heart_rate < 60 or heart_rate > 100

if __name__ == "__main__":
    print(f"Alert for HR 110: {is_alert_triggered(110)}")
