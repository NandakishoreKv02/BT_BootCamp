"""
Unit 1.4: Variables & Data Types - Exercises
Practice Python's type system, primitive types, type casting, and naming conventions.
"""

# ============================================================================
# Exercise 1: Variable Naming (PEP 8)
# ============================================================================

def exercise_1_fix_names():
    """
    TODO: Fix the variable names below to follow valid PEP 8 snake_case.
    Return the values in a dictionary with the CORRECT names as keys.
    """
    patient_name = "John Doe"
    patient_age = 45
    is_active = True
    max_heart_rate = 220
    
    return {
        "patient_name": patient_name,
        "patient_age": patient_age,
        "is_active": is_active,
        "max_heart_rate": max_heart_rate
    }


# ============================================================================
# Exercise 2: Type Inspection
# ============================================================================

def exercise_2_check_types(val1, val2, val3, val4):
    """
    TODO: Identify the types of the 4 arguments.
    Return a list of type objects (e.g., [int, str, ...]).
    
    Args:
        val1, val2, val3, val4: Any inputs
        
    Returns:
        list: A list containing type(val1), type(val2), etc.
    """
    return [type(val1), type(val2), type(val3), type(val4)]


# ============================================================================
# Exercise 3: Explicit Type Casting
# ============================================================================

def exercise_3_cast_inputs(age_str, height_str, weight_str):
    """
    TODO: Convert inputs to appropriate types.
    
    Args:
        age_str (str): e.g., "25" -> Convert to int
        height_str (str): e.g., "1.75" -> Convert to float
        weight_str (str): e.g., "70" -> Convert to float
        
    Returns:
        tuple: (age_int, height_float, weight_float)
    """
    return (int(age_str), float(height_str), float(weight_str))


# ============================================================================
# Exercise 4: String Manipulation
# ============================================================================

def exercise_4_format_record(first_name, last_name, id_num):
    """
    TODO: Create a formatted string.
    
    Args:
        first_name (str): "John"
        last_name (str): "Doe"
        id_num (int): 42
        
    Returns:
        str: "ID: 42 | Name: Doe, John" (Note: ID is int in args, needs to be in string)
    """
    return f"ID: {id_num} | Name: {last_name}, {first_name}"


# ============================================================================
# Exercise 5: Boolean Logic
# ============================================================================

def exercise_5_is_adult(age):
    """
    TODO: Check if age represents an adult (>= 18).
    
    Args:
        age (int or float)
        
    Returns:
        bool: True if age >= 18, else False
    """
    return age >= 18


# ============================================================================
# Exercise 6: Instance Checking
# ============================================================================

def exercise_6_safe_add(a, b):
    """
    TODO: Add two numbers, but ONLY if they are both numbers (int or float).
    Use isinstance() to check.
    
    Args:
        a, b: Any types
        
    Returns:
        The sum if both are numbers.
        None if either input is not a number.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return None


# ============================================================================
# Exercise 7: Mutability Check
# ============================================================================

def exercise_7_immutability_demo():
    """
    TODO: Demonstrate that integers are immutable.
    
    1. Create variable x = 10
    2. Store its id() in a variable id1
    3. Add 1 to x (x += 1)
    4. Store its new id() in a variable id2
    
    Returns:
        tuple: (id1, id2, are_different) -> (int, int, bool)
        are_different should be True
    """
    x = 10
    id1 = id(x)
    x += 1
    id2 = id(x)
    return (id1, id2, id1 != id2)


# ============================================================================
# Exercise 8: Handling Type Errors
# ============================================================================

def exercise_8_safe_convert(value):
    """
    TODO: Try to convert value to int.
    If it fails (ValueError or TypeError), return None.
    
    Args:
        value: Any input (str, float, list, etc.)
        
    Returns:
        int or None
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.4 Exercises...")
    passed = 0
    total = 8

    # Test 1
    try:
        res = exercise_1_fix_names()
        expected_keys = {'patient_name', 'patient_age', 'is_active', 'max_heart_rate'}
        if res and set(res.keys()) == expected_keys and res['patient_name'] == "John Doe":
            print("PASS: Exercise 1")
            passed += 1
        else:
            print(f"FAIL: Exercise 1 - Incorrect keys or values. Got: {res}")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        if exercise_2_check_types(1, 1.0, "s", True) == [int, float, str, bool]:
            print("PASS: Exercise 2")
            passed += 1
        else:
            print("FAIL: Exercise 2 - Incorrect types identified")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        res = exercise_3_cast_inputs("25", "1.75", "70")
        if res == (25, 1.75, 70.0) and isinstance(res[0], int) and isinstance(res[2], float):
            print("PASS: Exercise 3")
            passed += 1
        else:
            print(f"FAIL: Exercise 3 - Got {res}")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        if exercise_4_format_record("John", "Doe", 42) == "ID: 42 | Name: Doe, John":
            print("PASS: Exercise 4")
            passed += 1
        else:
            print(f"FAIL: Exercise 4 - Got '{exercise_4_format_record('John', 'Doe', 42)}'")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")

    # Test 5
    try:
        if exercise_5_is_adult(18) is True and exercise_5_is_adult(17) is False:
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        if exercise_6_safe_add(10, 20) == 30 and exercise_6_safe_add(10, "20") is None:
            print("PASS: Exercise 6")
            passed += 1
        else:
            print("FAIL: Exercise 6")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    # Test 7
    try:
        id1, id2, diff = exercise_7_immutability_demo()
        if diff is True and id1 != id2:
            print("PASS: Exercise 7")
            passed += 1
        else:
            print("FAIL: Exercise 7 - IDs should differ for immutable int")
    except Exception as e:
        print(f"ERROR: Exercise 7 - {e}")

    # Test 8
    try:
        if exercise_8_safe_convert("123") == 123 and exercise_8_safe_convert("abc") is None:
            print("PASS: Exercise 8")
            passed += 1
        else:
            print("FAIL: Exercise 8")
    except Exception as e:
        print(f"ERROR: Exercise 8 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
