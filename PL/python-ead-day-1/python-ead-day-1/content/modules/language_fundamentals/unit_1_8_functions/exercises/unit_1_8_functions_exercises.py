"""
Unit 1.8: Functions - Exercises
Practice defining, calling, and documenting functions.
"""

# ============================================================================
# Exercise 1: Basic Definition (Temp Conversion)
# ============================================================================

def celsius_to_fahrenheit(celsius):
    """
    TODO: Convert Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    
    Args:
        celsius (float)
        
    Returns:
        float: Fahrenheit value
    """
    # TODO: Implement formula
    return (celsius * 9/5) + 32


# ============================================================================
# Exercise 2: Default Parameters (Lab Urgency)
# ============================================================================

def format_lab_order(patient_name, test_type, is_urgent=False):
    """
    TODO: Return a string in the format:
    "Patient: {name}, Order: {type}, Priority: {priority}"
    Priority should be "STAT" if is_urgent is True, else "Routine".
    
    Args:
        patient_name (str)
        test_type (str)
        is_urgent (bool): Defaults to False
        
    Returns:
        str
    """
    # TODO: Implement formatting logic
    priority = "STAT" if is_urgent else "Routine"
    return f"Patient: {patient_name}, Order: {test_type}, Priority: {priority}"


# ============================================================================
# Exercise 3: Return Values (MAP Calculation)
# ============================================================================

def calculate_map(systolic, diastolic):
    """
    TODO: Calculate Mean Arterial Pressure (MAP).
    Formula: (systolic + 2 * diastolic) / 3
    
    Args:
        systolic (int)
        diastolic (int)
        
    Returns:
        float: Rounded to 1 decimal place.
    """
    # TODO: Implement formula
    return round((systolic + 2 * diastolic) / 3, 1)


# ============================================================================
# Exercise 4: Keyword Arguments (Medication Logic)
# ============================================================================

def prescribe_med(med_name, dose_mg, frequency, duration_days):
    """
    TODO: Return a prescription summary.
    "Prescribed {dose_mg}mg of {med_name}, {frequency}, for {duration_days} days."
    
    This function will be tested by calling it using KEYWORD arguments in the runner.
    """
    # TODO: Implement formatting
    return f"Prescribed {dose_mg}mg of {med_name}, {frequency}, for {duration_days} days."


# ============================================================================
# Exercise 5: Scope Challenge
# ============================================================================

app_name = "HealthVitals"

def get_app_info():
    """
    TODO: Extract the global app_name and a local version string.
    Return a tuple: (app_name, version)
    """
    version = "1.0.0"
    # TODO: Return tuple
    return (app_name, version)


# ============================================================================
# Exercise 6: Multiple Return Paths (Age Validator)
# ============================================================================

def validate_age_for_drug(age, min_age=18):
    """
    TODO: If age is less than min_age, return "Ineligible".
    Otherwise, return "Eligible".
    """
    # TODO: Implement if/else with returns
    if age < min_age:
        return "Ineligible"
    return "Eligible"


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.8 Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        if celsius_to_fahrenheit(0) == 32.0 and celsius_to_fahrenheit(100) == 212.0:
            print("PASS: Exercise 1")
            passed += 1
        else:
            print("FAIL: Exercise 1")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        if "STAT" in format_lab_order("A", "B", True) and "Routine" in format_lab_order("A", "B"):
            print("PASS: Exercise 2")
            passed += 1
        else:
            print("FAIL: Exercise 2")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        if calculate_map(120, 80) == 93.3:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print(f"FAIL: Exercise 3 - Got {calculate_map(120,80)}")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        res = prescribe_med(duration_days=7, med_name="A", dose_mg=5, frequency="QD")
        if "7 days" in res and "5mg" in res:
            print("PASS: Exercise 4")
            passed += 1
        else:
            print("FAIL: Exercise 4")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")

    # Test 5
    try:
        if get_app_info() == ("HealthVitals", "1.0.0"):
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        if validate_age_for_drug(15) == "Ineligible" and validate_age_for_drug(20) == "Eligible":
            print("PASS: Exercise 6")
            passed += 1
        else:
            print("FAIL: Exercise 6")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
