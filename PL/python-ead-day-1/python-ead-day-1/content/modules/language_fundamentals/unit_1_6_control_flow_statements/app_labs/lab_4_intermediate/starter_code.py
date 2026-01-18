"""
Lab 4: Lab Result Filter - Starter Code
"""

def sanitize_lab_results(raw_results):
    """
    Filter lab results using break and continue.
    
    Args:
        raw_results (list): Mixed data.
        
    Returns:
        list: Filtered numerical values.
    """
    # TODO: Implement loop with break and continue
    cleaned = []
    for item in raw_results:
        if item is None:
            continue
        if item == "CRITICAL_ERROR":
            break
        cleaned.append(item)
    return cleaned

if __name__ == "__main__":
    data = [10.5, None, 15.0, "CRITICAL_ERROR", 20.0]
    print(f"Sanitized: {sanitize_lab_results(data)}")
