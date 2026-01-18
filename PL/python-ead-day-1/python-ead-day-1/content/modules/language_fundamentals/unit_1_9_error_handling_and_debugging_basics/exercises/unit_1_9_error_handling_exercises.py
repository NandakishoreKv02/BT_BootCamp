"""
Unit 1.9: Error Handling & Debugging Basics - Exercises
Practice with try/except, error trapping, and resilience.
"""

# ============================================================================
# Exercise 1: Safe Division (Dosage Calc)
# ============================================================================

def safe_calculate_dose(total_mg, doses):
    """
    TODO: Calculate mg per dose (total_mg / doses).
    Use try/except to handle ZeroDivisionError.
    
    Args:
        total_mg (float)
        doses (int)
        
    Returns:
        float: Result if successful, or 0.0 if error occurs.
    """
    # TODO: Implement try/except
    try:
        return total_mg / doses
    except ZeroDivisionError:
        return 0.0


# ============================================================================
# Exercise 2: String to Float Conversion (Vital Parsing)
# ============================================================================

def parse_vital_reading(reading_str):
    """
    TODO: Convert reading_str to a float.
    Use try/except to handle ValueError (e.g. if string is "N/A").
    
    Args:
        reading_str (str)
        
    Returns:
        float or None: The float value, or None if conversion fails.
    """
    # TODO: Implement try/except
    try:
        return float(reading_str)
    except ValueError:
        return None


# ============================================================================
# Exercise 3: Dictionary Key Guard (Patient Search)
# ============================================================================

def get_patient_age(patient_dict):
    """
    TODO: Return the value for key "age".
    Use try/except to handle KeyError if "age" is missing.
    
    Args:
        patient_dict (dict)
        
    Returns:
        int or str: The age if found, "Unknown" if not found.
    """
    # TODO: Implement try/except
    try:
        return patient_dict["age"]
    except KeyError:
        return "Unknown"


# ============================================================================
# Exercise 4: List Index Guard (Recent Readings)
# ============================================================================

def get_last_reading(readings_list):
    """
    TODO: Return the last item (index -1) in the list.
    Use try/except to handle IndexError if the list is empty.
    
    Args:
        readings_list (list)
        
    Returns:
        float or str: The last value, or "No Data" if empty.
    """
    # TODO: Implement try/except
    try:
        return readings_list[-1]
    except IndexError:
        return "No Data"


# ============================================================================
# Exercise 5: Multiple Exception Types
# ============================================================================

def process_and_divide(data_list, index, divisor):
    """
    TODO: 
    1. Extract item from data_list at 'index'.
    2. Convert it to float.
    3. Divide by 'divisor'.
    
    Handle IndexError, ValueError, and ZeroDivisionError separately.
    
    Returns:
        The result or a specific error message string:
        - "ERROR_INDEX"
        - "ERROR_VALUE"
        - "ERROR_ZERO"
    """
    # TODO: Implement complex try/except
    try:
        value = data_list[index]
        value_float = float(value)
        return value_float / divisor
    except IndexError:
        return "ERROR_INDEX"
    except ValueError:
        return "ERROR_VALUE"
    except ZeroDivisionError:
        return "ERROR_ZERO"


# ============================================================================
# Exercise 6: The Finally Block (Cleanup)
# ============================================================================

def log_and_calculate(num1, num2):
    """
    TODO: 
    1. Try to add num1 and num2.
    2. In 'finally', return a tuple (result, "Operation Logged").
    
    If addition fails (TypeError), result should be 0.
    """
    # TODO: Implement try/except/finally
    result = 0
    try:
        result = num1 + num2
    except TypeError:
        result = 0
    finally:
        return (result, "Operation Logged")


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.9 Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        if safe_calculate_dose(100, 2) == 50.0 and safe_calculate_dose(100, 0) == 0.0:
            print("PASS: Exercise 1")
            passed += 1
        else:
            print("FAIL: Exercise 1")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        if parse_vital_reading("98.6") == 98.6 and parse_vital_reading("ERROR") is None:
            print("PASS: Exercise 2")
            passed += 1
        else:
            print(f"FAIL: Exercise 2")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        if get_patient_age({"age": 25}) == 25 and get_patient_age({}) == "Unknown":
            print("PASS: Exercise 3")
            passed += 1
        else:
            print("FAIL: Exercise 3")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        if get_last_reading([1.2, 5.5]) == 5.5 and get_last_reading([]) == "No Data":
            print("PASS: Exercise 4")
            passed += 1
        else:
            print("FAIL: Exercise 4")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")

    # Test 5
    try:
        res1 = process_and_divide([10], 0, 2) # 5.0
        res2 = process_and_divide([10], 5, 2) # ERROR_INDEX
        res3 = process_and_divide(["X"], 0, 2) # ERROR_VALUE
        res4 = process_and_divide([10], 0, 0) # ERROR_ZERO
        
        if res1 == 5.0 and res2 == "ERROR_INDEX" and res3 == "ERROR_VALUE" and res4 == "ERROR_ZERO":
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        res = log_and_calculate(5, 5)
        if res == (10, "Operation Logged"):
            print("PASS: Exercise 6")
            passed += 1
        else:
            print(f"FAIL: Exercise 6 - Got {res}")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
