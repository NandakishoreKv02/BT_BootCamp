"""
Unit 1.6: Control Flow Statements - Exercises
Practice if/elif/else, loops, and loop control.
"""

# ============================================================================
# Exercise 1: Triage Categorization
# ============================================================================

def categorize_vitals(heart_rate):
    """
    TODO: Categorize heart rate into triage levels.
    - HR < 60: "Bradycardia"
    - 60 <= HR <= 100: "Normal"
    - HR > 100: "Tachycardia"
    
    Args:
        heart_rate (int)
        
    Returns:
        str: The triage level
    """
    # TODO: Implement if/elif/else logic
    if heart_rate < 60:
        return "Bradycardia"
    elif heart_rate <= 100:
        return "Normal"
    else:
        return "Tachycardia"


# ============================================================================
# Exercise 2: Dose Count Generation
# ============================================================================

def get_even_dosages(max_dose):
    """
    TODO: Return a list of all even numbers from 2 up to max_dose (inclusive).
    Use range() and a loop.
    
    Args:
        max_dose (int): e.g. 10
        
    Returns:
        list: [2, 4, 6, 8, 10]
    """
    evens = []
    # TODO: Implement for loop with range
    for i in range(2, max_dose + 1, 2):
        evens.append(i)
    return evens


# ============================================================================
# Exercise 3: Patient Search (Break)
# ============================================================================

def find_patient_id(patient_list, target_name):
    """
    TODO: Find the index of target_name in patient_list.
    If found, return the index and STOP searching immediately (break).
    If not found after the whole loop, return -1.
    
    Args:
        patient_list (list): ["Alice", "Bob", "Charlie"]
        target_name (str): "Bob"
        
    Returns:
        int: Index of target, or -1
    """
    # TODO: Implement loop with break
    for i, name in enumerate(patient_list):
        if name == target_name:
            return i
    return -1


# ============================================================================
# Exercise 4: Data Sanitization (Continue)
# ============================================================================

def clean_reading_list(readings):
    """
    TODO: Calculate the sum of all valid readings in the list.
    - If a reading is 0 or negative, skip it using 'continue'.
    - If a reading is valid, add it to the sum.
    
    Args:
        readings (list): [72, -1, 80, 0, 95]
        
    Returns:
        int: Total sum of valid readings (72 + 80 + 95 = 247)
    """
    total = 0
    # TODO: Implement loop with continue
    for reading in readings:
        if reading <= 0:
            continue
        total += reading
    return total


# ============================================================================
# Exercise 5: Monitoring Simulation (While)
# ============================================================================

def monitor_until_stable(history):
    """
    TODO: Sum history values until you encounter a 0 (stable signal lost).
    Use a while loop.
    
    Args:
        history (list): [10, 20, 30, 0, 50, 60]
        
    Returns:
        int: Sum before the 0 (10 + 20 + 30 = 60)
    """
    total = 0
    i = 0
    # TODO: Implement while loop
    while i < len(history) and history[i] != 0:
        total += history[i]
        i += 1
    return total


# ============================================================================
# Exercise 6: Nested Logic (Ward Triage)
# ============================================================================

def scan_wards(hospital_wards):
    """
    TODO: Count how many 'Critical' patients are in 'Ward A'.
    
    Args:
        hospital_wards (dict): 
        {
            "Ward A": ["Stable", "Critical", "Critical"],
            "Ward B": ["Stable", "Critical"]
        }
        
    Returns:
        int: Number of critical patients in Ward A only.
    """
    count = 0
    # TODO: Implement nested logic (if Ward A, then loop and check status)
    if "Ward A" in hospital_wards:
        for status in hospital_wards["Ward A"]:
            if status == "Critical":
                count += 1
    return count


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.6 Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        if categorize_vitals(50) == "Bradycardia" and categorize_vitals(80) == "Normal":
            print("PASS: Exercise 1")
            passed += 1
        else:
            print("FAIL: Exercise 1")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        if get_even_dosages(10) == [2, 4, 6, 8, 10]:
            print("PASS: Exercise 2")
            passed += 1
        else:
            print("FAIL: Exercise 2")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        if find_patient_id(["A", "B", "C"], "B") == 1 and find_patient_id(["A"], "X") == -1:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print("FAIL: Exercise 3")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        if clean_reading_list([10, -5, 20, 0, 30]) == 60:
            print("PASS: Exercise 4")
            passed += 1
        else:
            print("FAIL: Exercise 4")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")

    # Test 5
    try:
        if monitor_until_stable([5, 5, 5, 0, 10]) == 15:
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        wards = {"Ward A": ["Critical", "Stable"], "Ward B": ["Critical"]}
        if scan_wards(wards) == 1:
            print("PASS: Exercise 6")
            passed += 1
        else:
            print("FAIL: Exercise 6")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
