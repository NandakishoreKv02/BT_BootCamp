"""
Unit 1.3: Python Program Structure - Exercises
Practice indentation, comments, docstrings, and the __main__ guard.
"""

# ============================================================================
# Exercise 1: Fix Indentation Errors
# ============================================================================

def exercise_1_starter():
    """
    TODO: Fix the indentation errors in this function.
    
    The function should:
    1. Check if temperature > 38.0
    2. If yes, check if heart_rate > 100
    3. Return appropriate messages
    """
    temperature = 37.5
    heart_rate = 95
    if temperature > 38.0:
        print("High fever")
        if heart_rate > 100:
            print("Also tachycardia")
    else:
        print("Normal temperature")
    return "Complete"


# ============================================================================
# Exercise 2: Add Proper Docstring
# ============================================================================

def exercise_2_starter(patient_id, name, age):
    """
    Create a patient record dictionary.
    
    Args:
        patient_id (int): Unique patient identifier.
        name (str): Patient's full name.
        age (int): Patient's age in years.
    
    Returns:
        dict: Patient record with id, name, and age.
    """
    patient = {
        "id": patient_id,
        "name": name,
        "age": age
    }
    return patient


# ============================================================================
# Exercise 3: Implement __main__ Guard
# ============================================================================

def calculate_dosage(weight_kg, mg_per_kg):
    """Calculate medication dosage based on weight."""
    return weight_kg * mg_per_kg

if __name__ == "__main__":
    result = calculate_dosage(70, 15)
    print(result)


# ============================================================================
# Exercise 4: Create a Reusable Module Function
# ============================================================================

def exercise_4_starter(patient_id):
    """
    TODO: Create a function that formats patient IDs.
    
    Format: PAT-XXXXX (5 digits with leading zeros)
    Example: 42 -> PAT-00042
    
    Args:
        patient_id (int): Numeric patient ID
    
    Returns:
        str: Formatted patient ID
    """
    return f"PAT-{patient_id:05d}"


# ============================================================================
# Exercise 5: Add Comments and Docstrings
# ============================================================================

def exercise_5_starter(birth_year):
    """
    Calculate age from birth year.
    
    Args:
        birth_year (int): Year of birth.
    
    Returns:
        int: Current age in years.
    """
    import datetime
    # Get current year from system datetime
    current_year = datetime.datetime.now().year
    # Calculate age by subtracting birth year from current year
    age = current_year - birth_year
    return age


# ============================================================================
# Exercise 6: Nested Indentation
# ============================================================================

def exercise_6_starter(temperature, heart_rate, blood_pressure):
    """
    TODO: Implement proper nested indentation for vital signs check.
    
    Logic:
    - If temperature > 38.0:
        - If heart_rate > 100:
            - Return "Critical"
        - Else:
            - Return "High Fever"
    - Elif heart_rate > 100:
        - Return "Tachycardia"
    - Elif blood_pressure > 140:
        - Return "Hypertension"
    - Else:
        - Return "Normal"
    """
    if temperature > 38.0:
        if heart_rate > 100:
            return "Critical"
        else:
            return "High Fever"
    elif heart_rate > 100:
        return "Tachycardia"
    elif blood_pressure > 140:
        return "Hypertension"
    else:
        return "Normal"


# ============================================================================
# Exercise 7: Module Structure
# ============================================================================

# TODO: Organize this code properly:
# 1. Add module docstring at the top
# 2. Group imports
# 3. Define constants
# 4. Define functions
# 5. Add __main__ guard

"""
Patient management utilities.
"""

import random
import datetime

MAX_PATIENTS = 100

def generate_patient_id():
    return random.randint(1000, 9999)

def get_current_timestamp():
    return datetime.datetime.now()

if __name__ == "__main__":
    print("Module loaded")


# ============================================================================
# Exercise 8: Docstring Formats
# ============================================================================

def exercise_8_starter(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.
    
    Returns:
        float: BMI value.
    
    Raises:
        ValueError: If weight or height is not positive.
    
    Example:
        >>> exercise_8_starter(70, 1.75)
        22.857142857142858
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    return weight / (height ** 2)


# ============================================================================
# Exercise 9: Script vs Module
# ============================================================================

def exercise_9_starter():
    """
    TODO: Make this function work both as a script and importable module.
    
    When run as script: Print "Running as script"
    When imported: Do nothing
    """
    pass

if __name__ == "__main__":
    print("Running as script")


# ============================================================================
# Exercise 10: Complete Program Structure
# ============================================================================

# TODO: Create a complete, well-structured program that:
# 1. Has a module docstring
# 2. Imports (if needed)
# 3. Constants
# 4. Helper functions with docstrings
# 5. Main function
# 6. __main__ guard
#
# Program purpose: Patient registration system
# Should have:
# - register_patient(name, age) function
# - validate_age(age) function (must be 0-120)
# - Main function that registers 2 test patients

"""
Patient Registration System.
"""

MIN_AGE = 0
MAX_AGE = 120

def validate_age(age):
    """
    Validate patient age.
    
    Args:
        age (int): Patient age.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    return MIN_AGE <= age <= MAX_AGE

def register_patient(name, age):
    """
    Register a new patient.
    
    Args:
        name (str): Patient name.
        age (int): Patient age.
    
    Returns:
        dict: Patient record if valid, None otherwise.
    """
    if validate_age(age):
        return {"name": name, "age": age}
    return None

def main():
    """Main function to register test patients."""
    patient1 = register_patient("John Doe", 35)
    patient2 = register_patient("Jane Smith", 28)
    print(patient1)
    print(patient2)

if __name__ == "__main__":
    main()


# ============================================================================
# Test Runner
# ============================================================================

def test_exercise_1():
    """Test indentation fix."""
    try:
        result = exercise_1_starter()
        assert result == "Complete"
        print("PASS: Exercise 1")
    except (IndentationError, SyntaxError) as e:
        print(f"FAIL: Exercise 1 - {e}")

def test_exercise_4():
    """Test patient ID formatting."""
    result = exercise_4_starter(42)
    assert result == "PAT-00042", f"Expected 'PAT-00042', got '{result}'"
    result = exercise_4_starter(12345)
    assert result == "PAT-12345", f"Expected 'PAT-12345', got '{result}'"
    print("PASS: Exercise 4")

def test_exercise_6():
    """Test nested indentation logic."""
    assert exercise_6_starter(39.0, 110, 120) == "Critical"
    assert exercise_6_starter(39.0, 80, 120) == "High Fever"
    assert exercise_6_starter(37.0, 110, 120) == "Tachycardia"
    assert exercise_6_starter(37.0, 80, 150) == "Hypertension"
    assert exercise_6_starter(37.0, 80, 120) == "Normal"
    print("PASS: Exercise 6")

if __name__ == "__main__":
    print("Running Unit 1.3 Exercises...\n")
    
    # Run tests
    tests = [test_exercise_1, test_exercise_4, test_exercise_6]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__} - {e}")
        except Exception as e:
            print(f"ERROR: {test.__name__} - {e}")
    
    print(f"\nResult: {passed}/{len(tests)} tests passed.")
