"""
Unit 1.7: Core Built-in Data Structures - Exercises
Practice with Lists, Tuples, Sets, and Dictionaries.
"""

# ============================================================================
# Exercise 1: List Operations (Pharmacy Inventory)
# ============================================================================

def manage_inventory(meds, new_med, remove_med):
    """
    TODO: Perform the following on the 'meds' list:
    1. Append 'new_med'.
    2. Sort the list alphabetically.
    3. Remove 'remove_med' if it exists.
    
    Args:
        meds (list): ["Aspirin", "Ibuprofen"]
        new_med (str): "Metformin"
        remove_med (str): "Aspirin"
        
    Returns:
        list: The updated meds list
    """
    # TODO: Implement list methods
    meds.append(new_med)
    meds.sort()
    if remove_med in meds:
        meds.remove(remove_med)
    return meds


# ============================================================================
# Exercise 2: Tuple Unpacking (Patient Records)
# ============================================================================

def get_patient_summary(patient_data):
    """
    TODO: 'patient_data' is a tuple (name, age, blood_type).
    Unpack the tuple and return a formatted string:
    "Patient {name} is {age} years old with blood type {blood_type}."
    
    Args:
        patient_data (tuple): ("John Doe", 45, "A+")
        
    Returns:
        str
    """
    # TODO: Unpack and format
    name, age, blood_type = patient_data
    return f"Patient {name} is {age} years old with blood type {blood_type}."


# ============================================================================
# Exercise 3: Set Operations (Distinct Diagnoses)
# ============================================================================

def find_common_diagnoses(ward_a, ward_b):
    """
    TODO: Find diagnoses that appear in BOTH ward lists.
    Use set intersection.
    
    Args:
        ward_a (list): ["Flu", "COVID", "Cold"]
        ward_b (list): ["Flu", "Broken Arm"]
        
    Returns:
        set: Results
    """
    # TODO: Convert to sets and find intersection
    return set(ward_a) & set(ward_b)


# ============================================================================
# Exercise 4: Dictionary Mapping (MRN Lookup)
# ============================================================================

def update_patient_record(records, mrn, new_status):
    """
    TODO: Update the status of a patient in the records dictionary.
    Each record is: {mrn: {"name": "...", "status": "..."}}
    
    1. If mrn exists, update its "status" to new_status.
    2. If mrn doesn't exist, return None. Otherwise return updated record.
    
    Args:
        records (dict)
        mrn (str)
        new_status (str)
        
    Returns:
        dict or None
    """
    # TODO: Dictionary key update
    if mrn in records:
        records[mrn]["status"] = new_status
        return records[mrn]
    return None


# ============================================================================
# Exercise 5: Deeply Nested Access
# ============================================================================

def get_systolic_bp(patient):
    """
    TODO: Extract the systolic blood pressure from a complex dictionary.
    Structure: {"data": {"vitals": {"bp": [systolic, diastolic]}}}
    
    Args:
        patient (dict)
        
    Returns:
        int: The first element in the bp list.
    """
    # TODO: Access nested keys
    return patient["data"]["vitals"]["bp"][0]


# ============================================================================
# Exercise 6: Set Deduplication
# ============================================================================

def get_unique_tags(tags_list):
    """
    TODO: Return a sorted list of unique tags.
    
    Args:
        tags_list (list): ["Urgent", "Routine", "Urgent"]
        
    Returns:
        list: ["Routine", "Urgent"]
    """
    # TODO: Use set for uniqueness then sort
    return sorted(set(tags_list))


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.7 Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        res = manage_inventory(["Z", "A"], "B", "Z")
        if "B" in res and "A" in res and "Z" not in res and res == sorted(res):
            print("PASS: Exercise 1")
            passed += 1
        else:
            print(f"FAIL: Exercise 1 - Got {res}")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        res = get_patient_summary(("Alice", 30, "O-"))
        if "Alice" in res and "30" in res and "O-" in res:
            print("PASS: Exercise 2")
            passed += 1
        else:
            print("FAIL: Exercise 2")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        if find_common_diagnoses(["A", "B"], ["B", "C"]) == {"B"}:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print("FAIL: Exercise 3")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        records = {"1": {"status": "Stable"}}
        res = update_patient_record(records, "1", "Discharged")
        if res and res["status"] == "Discharged":
            print("PASS: Exercise 4")
            passed += 1
        else:
            print("FAIL: Exercise 4")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")

    # Test 5
    try:
        patient = {"data": {"vitals": {"bp": [120, 80]}}}
        if get_systolic_bp(patient) == 120:
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        if get_unique_tags(["A", "B", "A"]) == ["A", "B"]:
            print("PASS: Exercise 6")
            passed += 1
        else:
            print("FAIL: Exercise 6")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
