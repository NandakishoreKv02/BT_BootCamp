"""
Lab 1: Triage Level Classifier - Starter Code
"""

def classify_triage(heart_rate):
    """
    Classify patient triage level based on heart rate.
    
    Args:
        heart_rate (int)
        
    Returns:
        str: "RED", "YELLOW", or "GREEN"
    """
    if heart_rate > 140 or heart_rate < 40:
        return "RED"
    elif heart_rate > 110 or heart_rate < 50:
        return "YELLOW"
    else:
        return "GREEN"

if __name__ == "__main__":
    print(f"HR 150: {classify_triage(150)}")
    print(f"HR 80: {classify_triage(80)}")
