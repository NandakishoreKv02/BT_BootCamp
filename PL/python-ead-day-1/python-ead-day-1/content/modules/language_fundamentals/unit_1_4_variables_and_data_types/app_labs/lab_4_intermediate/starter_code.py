"""
Lab 4: Data Cleaner - Starter Code
"""

def calculate_average_hr(data_list):
    """
    Calculate average integer heart rate from mixed data.
    
    Args:
        data_list (list): Mixed types [int, str, None, ...]
        
    Returns:
        float: Average, or 0.0 if empty/no valid data.
    """
    valid_sum = 0
    valid_count = 0
    
    for item in data_list:
        if isinstance(item, int):
            valid_sum += item
            valid_count += 1
        elif isinstance(item, str):
            try:
                valid_sum += int(item)
                valid_count += 1
            except ValueError:
                pass
    
    return valid_sum / valid_count if valid_count > 0 else 0.0

if __name__ == "__main__":
    test_data = [80, "90", "ERR", None, 70, 72.5] # 72.5 should probably be ignored or casted? Instruction says 'ints' generally.
    print(f"Average: {calculate_average_hr(test_data)}")
