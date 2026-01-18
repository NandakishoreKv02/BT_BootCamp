"""
Unit 1.12: Hands-on Labs & Exercises
Comprehensive integration exercises combining all Python fundamentals.
"""

# ============================================================================
# Exercise 1: Patient Record Builder (Variables + Dictionaries + Functions)
# ============================================================================

def create_patient_record(mrn, name, age, diagnosis):
    """
    Create a structured patient dictionary.
    
    Args:
        mrn (str): Medical Record Number
        name (str): Patient full name
        age (int): Patient age
        diagnosis (str): Primary diagnosis
    
    Returns:
        dict: Complete patient record
    """
    # TODO: Return a dictionary with keys: "mrn", "name", "age", "diagnosis"
    return {"mrn": mrn, "name": name, "age": age, "diagnosis": diagnosis}


# ============================================================================
# Exercise 2: Vital Signs Validator (Control Flow + Error Handling)
# ============================================================================

def validate_vitals(temperature, heart_rate, systolic_bp):
    """
    Check if vitals are within normal ranges.
    
    Normal ranges:
    - Temperature: 36.1 - 37.2°C
    - Heart Rate: 60 - 100 bpm
    - Systolic BP: 90 - 120 mmHg
    
    Returns:
        list: List of abnormal vital names (e.g., ["temperature", "heart_rate"])
    """
    # TODO: Implement validation logic
    abnormal = []
    if not (36.1 <= temperature <= 37.2):
        abnormal.append("temperature")
    if not (60 <= heart_rate <= 100):
        abnormal.append("heart_rate")
    if not (90 <= systolic_bp <= 120):
        abnormal.append("systolic_bp")
    return abnormal


# ============================================================================
# Exercise 3: Medication List Processor (Lists + Loops)
# ============================================================================

def count_medications_by_type(medication_list, med_type):
    """
    Count how many medications of a specific type exist.
    
    Args:
        medication_list (list): List of medication dictionaries
            Each dict has keys: "name", "type", "dosage"
        med_type (str): Type to count (e.g., "antibiotic")
    
    Returns:
        int: Count of medications matching the type
    """
    # TODO: Implement counting logic
    count = 0
    for med in medication_list:
        if med["type"] == med_type:
            count += 1
    return count


# ============================================================================
# Exercise 4: Lab Result Analyzer (Functions + Data Structures)
# ============================================================================

def analyze_lab_results(results):
    """
    Calculate statistics for a list of numeric lab results.
    
    Args:
        results (list): List of float values
    
    Returns:
        dict: {"average": float, "min": float, "max": float, "count": int}
    """
    # TODO: Implement statistical analysis
    if not results:
        return {"average": 0, "min": 0, "max": 0, "count": 0}
    return {
        "average": sum(results) / len(results),
        "min": min(results),
        "max": max(results),
        "count": len(results)
    }


# ============================================================================
# Exercise 5: Appointment Scheduler (Dictionaries + Control Flow)
# ============================================================================

def find_available_slot(schedule, requested_time):
    """
    Check if a time slot is available.
    
    Args:
        schedule (dict): {time: patient_name} e.g., {"09:00": "John", "10:00": None}
        requested_time (str): Time to check (e.g., "11:00")
    
    Returns:
        bool: True if available (None or not in dict), False otherwise
    """
    # TODO: Implement availability check
    return requested_time not in schedule or schedule[requested_time] is None


# ============================================================================
# Exercise 6: Patient Data File Writer (I/O + Functions)
# ============================================================================

def save_patient_summary(filename, patient_data):
    """
    Write patient summary to a text file.
    
    Args:
        filename (str): Output file path
        patient_data (dict): Patient information
    
    Format:
        MRN: [mrn]
        Name: [name]
        Age: [age]
    """
    # TODO: Implement file writing
    with open(filename, 'w') as f:
        f.write(f"MRN: {patient_data['mrn']}\n")
        f.write(f"Name: {patient_data['name']}\n")
        f.write(f"Age: {patient_data['age']}\n")


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.12 Integration Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        record = create_patient_record("MRN001", "Jane Doe", 45, "Hypertension")
        if record.get("mrn") == "MRN001" and record.get("age") == 45:
            print("PASS: Exercise 1")
            passed += 1
        else:
            print("FAIL: Exercise 1")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        abnormal = validate_vitals(38.5, 110, 85)
        if "temperature" in abnormal and "heart_rate" in abnormal and "systolic_bp" in abnormal:
            print("PASS: Exercise 2")
            passed += 1
        else:
            print(f"FAIL: Exercise 2 - Got {abnormal}")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        meds = [
            {"name": "Amoxicillin", "type": "antibiotic", "dosage": "500mg"},
            {"name": "Ibuprofen", "type": "painkiller", "dosage": "200mg"},
            {"name": "Penicillin", "type": "antibiotic", "dosage": "250mg"}
        ]
        count = count_medications_by_type(meds, "antibiotic")
        if count == 2:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print(f"FAIL: Exercise 3 - Expected 2, got {count}")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        stats = analyze_lab_results([10.0, 20.0, 30.0])
        if stats.get("average") == 20.0 and stats.get("count") == 3:
            print("PASS: Exercise 4")
            passed += 1
        else:
            print(f"FAIL: Exercise 4 - Got {stats}")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")

    # Test 5
    try:
        schedule = {"09:00": "Alice", "10:00": None, "11:00": "Bob"}
        if find_available_slot(schedule, "10:00") and not find_available_slot(schedule, "09:00"):
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        import os
        test_file = "test_patient.txt"
        save_patient_summary(test_file, {"mrn": "TEST", "name": "Test", "age": 30})
        if os.path.exists(test_file):
            with open(test_file) as f:
                content = f.read()
            if "TEST" in content:
                print("PASS: Exercise 6")
                passed += 1
            else:
                print("FAIL: Exercise 6")
            os.remove(test_file)
        else:
            print("FAIL: Exercise 6 - File not created")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
