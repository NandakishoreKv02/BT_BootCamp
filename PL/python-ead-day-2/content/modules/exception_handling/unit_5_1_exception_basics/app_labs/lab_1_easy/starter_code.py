def safe_int_conversion(value):
    """
    TODO: 
    1. Try to return int(value).
    2. Catch ValueError and return None.
    """
    # WRITE CODE HERE
    pass

def safe_float_conversion(value):
    """
    TODO: 
    1. Try to return float(value).
    2. Catch ValueError and return None.
    """
    # WRITE CODE HERE
    pass

def process_intake(raw_data):
    """
    TODO:
    1. Validate 'age' using safe_int_conversion.
    2. Validate 'weight' using safe_float_conversion.
    3. If errors, return (None, [list_of_errors]).
    4. If success, return ({"age": int_val, "weight": float_val}, []).
    """
    errors = []
    clean_data = {}
    
    # WRITE CODE HERE
    
    if errors:
        return None, errors
    return clean_data, []

def main():
    # Test valid
    print(process_intake({"age": "30", "weight": "70.5"}))
    # Test invalid
    print(process_intake({"age": "old", "weight": "N/A"}))

if __name__ == "__main__":
    main()
