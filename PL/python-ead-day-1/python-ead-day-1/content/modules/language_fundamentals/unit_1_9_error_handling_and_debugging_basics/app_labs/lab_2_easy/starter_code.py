"""
Lab 2: Lab Result History Navigator - Starter Code
"""

def get_historical_result(results_list, offset):
    """
    Retrieve result at index 'offset'.
    
    Returns:
        The value or "Result Not Available".
    """
    try:
        return results_list[offset]
    except IndexError:
        return "Result Not Available"

if __name__ == "__main__":
    data = [12.5, 13.0, 11.2]
    print(f"Index 1: {get_historical_result(data, 1)}")
    print(f"Index 5: {get_historical_result(data, 5)}")
