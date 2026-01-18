"""
Lab 5: Lab Result Batch Processor - Starter Code
"""

def analyze_batch(batch, test_type, threshold):
    """
    Filter, transform, and aggregate a batch of lab results.
    
    Args:
        batch (list): List of dicts.
        test_type (str): Key to filter by.
        threshold (float): Alert limit.
        
    Returns:
        tuple: (float_avg, list_of_modified_dicts)
    """
    # TODO: Implement filtering, alerts, and average
    filtered_results = []
    for item in batch:
        if item["type"] == test_type:
            filtered_results.append(item)
    
    for result in filtered_results:
        if result["val"] > threshold:
            result["is_alert"] = True
        else:
            result["is_alert"] = False
    
    if len(filtered_results) > 0:
        total = sum(result["val"] for result in filtered_results)
        average = total / len(filtered_results)
    else:
        average = 0.0
    
    return (average, filtered_results)

if __name__ == "__main__":
    data = [
        {"type": "Glucose", "val": 95},
        {"type": "Glucose", "val": 150},
        {"type": "SPO2", "val": 98}
    ]
    avg, filtered = analyze_batch(data, "Glucose", 140)
    print(f"Average: {avg}")
    print(f"Details: {filtered}")
