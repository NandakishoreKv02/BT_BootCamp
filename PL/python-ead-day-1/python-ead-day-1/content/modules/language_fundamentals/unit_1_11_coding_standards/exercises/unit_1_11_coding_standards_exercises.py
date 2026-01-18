"""
Unit 1.11: Python Coding Standards & Best Practices - Exercises
Refactor and organize code according to PEP 8 and Pythonic principles.
"""

# ============================================================================
# Exercise 1: Professional Naming (Variables)
# ============================================================================

# TODO: Refactor these "Bad" names to PEP 8 standard (snake_case)
# and meaningful descriptors.

# p = "John Smith"
# a = 45
# is_A = True # represents 'is admitted'

def get_patient_info():
    """Returns a tuple of the refactored variables."""
    # TODO: define your refactored variables here
    patient_full_name = "John Smith"
    # Replace these:
    patient_age = 45
    is_admitted = True
    
    return (patient_full_name, patient_age, is_admitted)


# ============================================================================
# Exercise 2: Professional Naming (Functions)
# ============================================================================

# TODO: Rename this function to follow PEP 8 (snake_case)
def calculate_bmi(W, H):
    """
    Calculate Body Mass Index.
    """
    return W / (H ** 2)


# ============================================================================
# Exercise 3: Constants & Magic Numbers
# ============================================================================

# TODO: Define a constant for the conversion factor from Lbs to Kg (0.453592)
# and use it in the function.
LBS_TO_KG = 0.453592

def convert_to_kg(lbs):
    # TODO: Replace 0.45 with your constant
    return lbs * LBS_TO_KG


# ============================================================================
# Exercise 4: Class Naming
# ============================================================================

# TODO: Refactor this class name to follow PEP 8 (PascalCase)
class PatientEhrRecord:
    def __init__(self, mrn):
        self.mrn = mrn


# ============================================================================
# Exercise 5: Pythonic Membership
# ============================================================================

def is_allergy_present(allergy_to_find, patient_allergies):
    """
    TODO: Refactor this to be "Pythonic" using the 'in' keyword.
    Don't use a manual loop.
    """
    # for i in range(len(patient_allergies)):
    #     if patient_allergies[i] == allergy_to_find:
    #         return True
    # return False
    return allergy_to_find in patient_allergies


# ============================================================================
# Exercise 6: Script Organization
# ============================================================================

# TODO: move the print statement inside a proper 
# "if __name__ == '__main__':" block.

def medical_utility():
    return "Utility Ready"

# print(medical_utility()) # Move this!

if __name__ == "__main__":
    print(medical_utility())


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.11 Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        res = get_patient_info()
        if len(res) == 3 and res[0] == "John Smith":
            print("PASS: Exercise 1")
            passed += 1
        else:
            print("FAIL: Exercise 1")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        # We are checking if the snake_case version exists
        import sys
        current_module = sys.modules[__name__]
        if hasattr(current_module, 'calculate_bmi'):
            print("PASS: Exercise 2")
            passed += 1
        else:
            print("FAIL: Exercise 2 (Function not renamed to calculate_bmi)")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        import sys
        current_module = sys.modules[__name__]
        # Check for any uppercase constant and correct math
        constants = [name for name in dir(current_module) if name.isupper()]
        if len(constants) > 0 and round(convert_to_kg(100), 1) == 45.4:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print("FAIL: Exercise 3")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        import sys
        current_module = sys.modules[__name__]
        if hasattr(current_module, 'PatientEhrRecord'):
            print("PASS: Exercise 4")
            passed += 1
        else:
            print("FAIL: Exercise 4")
    except Exception as e:
        print(f"ERROR: Exercise 4")

    # Test 5
    try:
        if is_allergy_present("Peanuts", ["Latex", "Peanuts"]) == True:
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5")

    # Test 6
    try:
        # This is hard to test programmatically, so we'll check for the variable
        if "__name__" in open(__file__).read():
            print("PASS: Exercise 6")
            passed += 1
        else:
            print("FAIL: Exercise 6")
    except Exception as e:
        print(f"ERROR: Exercise 6")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
