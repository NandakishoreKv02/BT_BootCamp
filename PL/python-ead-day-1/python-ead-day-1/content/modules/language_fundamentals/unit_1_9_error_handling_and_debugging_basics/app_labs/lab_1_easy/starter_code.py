"""
Lab 1: Patient Weight Input Guard - Starter Code
"""

def parse_weight(input_str):
    """
    Safely convert weight string to float.
    
    Returns:
        float: The numeric weight or 0.0 if invalid.
    """
    try:
        return float(input_str)
    except ValueError:
        print(f"Invalid weight input: {input_str}")
        return 0.0

if __name__ == "__main__":
    print(f"Result 1: {parse_weight('75.5')}")
    print(f"Result 2: {parse_weight('not_a_number')}")
