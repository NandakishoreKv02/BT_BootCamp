"""
Lab 5: The SRP Specialist - Starter Code
"""

def clean_data(raw_list):
    # TODO: Implement
    cleaned = []
    for x in raw_list:
        try:
            cleaned.append(float(x))
        except ValueError:
            pass
    return cleaned

def analyze_risk(values):
    # TODO: Implement
    for value in values:
        if value > 140.0:
            return "HIGH"
    return "NORMAL"

def format_outcome(status):
    # TODO: Implement
    return f"SYSTEM REPORT: Status is {status}"

def process_labs(raw_list):
    """
    The orchestrator that uses the helpers.
    """
    # TODO: Connect the helpers
    cleaned = clean_data(raw_list)
    risk = analyze_risk(cleaned)
    return format_outcome(risk)

if __name__ == "__main__":
    raw = ["120", "ERROR", "150"]
    print(process_labs(raw))
