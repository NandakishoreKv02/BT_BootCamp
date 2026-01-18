"""
Unit 2.1: From Procedural to Object-Oriented Thinking - Exercises
Focus: Identifying procedural limitations and grouping state/behavior.
Note: We are NOT using 'class' yet. We are learning to structure data like objects.
"""

# ============================================================================
# Exercise 1: The Global State Trap (Healthcare Domain)
# ============================================================================
# CONTEXT: In clinical software, relying on global state is dangerous. If two 
# different parts of the app think they are managing the "current patient", 
# one might overwrite the other's data (e.g., ordering meds for the wrong person).
#
# MISSION: Fix the scoping issue. In Python, you cannot modify a global variable 
# from inside a function unless you explicitly declare it using the 'global' keyword.

current_patient_id = None
current_patient_status = "Waiting"

def admit_patient(patient_id):
    """
    Admit a patient by updating the global variables.
    
    Args:
        patient_id (str): The ID of the patient to admit (e.g., "MRN123")
        
    Requirement:
        1. Use the 'global' keyword to access 'current_patient_id' and 'current_patient_status'.
        2. Set 'current_patient_id' to the passed argument.
        3. Set 'current_patient_status' to "Admitted".
    """
    # TODO: Fix this function to update the global variables
    global current_patient_id, current_patient_status
    if current_patient_status == "Waiting":
        current_patient_id = patient_id
        current_patient_status = "Admitted"
    else:
        print("Bed is occupied!")

# ============================================================================
# Exercise 2: Grouping Data (The Proto-Object)
# ============================================================================
# CONTEXT: "Parallel Arrays" is a procedural anti-pattern where related data is 
# stored in separate lists. If you sort or filter one list, the others break.
#
# MISSION: Refactor these into "Proto-Objects" (Dictionaries). Individual 
# variables that "belong" together should live together in a single structure.

mrns = ["MRN001", "MRN002", "MRN003"]
names = ["Alice Smith", "Bob Jones", "Carol White"]
priorities = ["High", "Low", "Medium"]

def group_patient_data():
    """
    Convert the separate lists (mrns, names, priorities) into a single list of dicts.
    
    Returns:
        list: A list of dictionaries. 
              Example structure: {"mrn": "MRN001", "name": "Alice Smith", "priority": "High"}
              
    Instructions:
        1. Create an empty list called 'patients'.
        2. Use a loop (range(len(mrns))) to iterate through the lists.
        3. In each iteration, create a dictionary with the keys: 'mrn', 'name', 'priority'.
        4. Append that dictionary to your 'patients' list.
    """
    # TODO: Implement this
    return [{"mrn": mrns[i], "name": names[i], "priority": priorities[i]} for i in range(len(mrns))]

# ============================================================================
# Exercise 3: Encapsulation (Passing State Explicitly)
# ============================================================================
# CONTEXT: Instead of global variables, we pass "Objects" (dictionaries) into 
# functions. This ensures the function only touches the data it is given.
#
# MISSION: Write a "mutator" function that modifies the state of a patient record.

def update_vitals(patient_record, heart_rate, temp_c):
    """
    Update the vital signs stored inside a patient record.
    
    Args:
        patient_record (dict): A dictionary representing a patient.
                               Example: {'name': 'John', 'vitals': {}}
        heart_rate (int): New heart rate value.
        temp_c (float): New temperature value.
        
    Instructions:
        1. Access the 'vitals' key inside the patient_record (it's a nested dict).
        2. Set 'heart_rate' and 'temp_c' inside that nested dictionary.
        3. Return the modified patient_record.
    """
    # TODO: Implement this
    patient_record['vitals']['heart_rate'] = heart_rate
    patient_record['vitals']['temp_c'] = temp_c
    return patient_record

# ============================================================================
# Exercise 4: Identifying Nouns (System Analysis)
# ============================================================================
# CONTEXT: The first step in OOP design is finding the "Actors" or "Entities".
#
# MISSION: Extract potential software objects from a business requirement.
# Requirement: "A Doctor prescribes a Medication to a Patient, and the Pharmacist verifies the Dosage."

def extract_system_objects():
    """
    Identify potential Objects (Nouns) from the requirement above.
    
    Returns:
        list: At least 4 strings (e.g., ["Doctor", ...])
    """
    # TODO: Return a list of at least 4 nouns
    return ["Doctor", "Medication", "Patient", "Pharmacist", "Dosage"]

# ============================================================================
# Exercise 5: Stateless vs Stateful
# ============================================================================
# CONTEXT: Not everything should be an Object. 
# "Stateful" = Needs to remember history (Complex, use OOP).
# "Stateless" = Pure calculation (Simple, use Functions).

def is_stateful_candidate(concept_name):
    """
    Decide if a concept is an Object candidate (True) or Function candidate (False).
    
    Args:
        concept_name (str): Concept to evaluate.
        
    Logic:
        - "Patient Chart": Stateful (Object) -> Needs to store history.
        - "BMI Calculator": Stateless (Function) -> Just math on inputs.
    """
    # TODO: Return True for "Patient Chart", False for "BMI Calculator"
    return concept_name == "Patient Chart"

# ============================================================================
# Exercise 6: The Constructor Pattern (Encapsulated Factory)
# ============================================================================
# CONTEXT: To ensure all objects have the same "shape", we use Factory functions.
# This prevents different parts of the code from using different key names.

def create_prescription(drug_name, dosage, frequency):
    """
    Create a standardized prescription dictionary.
    
    Returns:
        dict: Keys must be 'drug', 'dosage', 'freq', 'status' (default 'Active').
    """
    # TODO: Implement this
    return {"drug": drug_name, "dosage": dosage, "freq": frequency, "status": "Active"}

def discontinue_prescription(prescription):
    """
    Change the status of a prescription object.
    
    Args:
        prescription (dict): The object to modify.
    """
    # TODO: Set status to 'Discontinued'
    prescription['status'] = "Discontinued"

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.1 Integration Exercises (Healthcare Domain)...")
    passed = 0
    total = 6

    # Test 1
    try:
        global current_patient_id, current_patient_status
        current_patient_id = None
        current_patient_status = "Waiting"
        try:
            admit_patient("MRN999")
            if current_patient_id == "MRN999" and current_patient_status == "Admitted":
                print("PASS: Exercise 1")
                passed += 1
            else:
                print(f"FAIL: Exercise 1 - Global state not updated. ID: {current_patient_id}, Status: {current_patient_status}")
        except UnboundLocalError:
             print("FAIL: Exercise 1 - UnboundLocalError (You forgot the 'global' keyword!)")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        patients = group_patient_data()
        if isinstance(patients, list) and len(patients) == 3:
            p1 = patients[0]
            if p1['mrn'] == "MRN001" and p1['name'] == "Alice Smith" and p1['priority'] == "High":
                print("PASS: Exercise 2")
                passed += 1
            else:
                print(f"FAIL: Exercise 2 - Incorrect structure: {p1}")
        else:
            print("FAIL: Exercise 2 - Expected list of length 3")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3
    try:
        p_rec = {'name': 'Test', 'vitals': {}}
        update_vitals(p_rec, 80, 37.5)
        if p_rec['vitals'].get('heart_rate') == 80 and p_rec['vitals'].get('temp_c') == 37.5:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print(f"FAIL: Exercise 3 - Vitals not updated correctly: {p_rec}")
    except Exception as e:
        print(f"ERROR: Exercise 3 - {e}")

    # Test 4
    try:
        nouns = extract_system_objects()
        expected = ["doctor", "patient", "medication", "pharmacist", "dosage"]
        student_nouns = [n.lower() for n in nouns]
        matches = set(student_nouns).intersection(expected)
        if len(matches) >= 4:
            print("PASS: Exercise 4")
            passed += 1
        else:
            print(f"FAIL: Exercise 4 - Found {nouns}, expected at least 4 from {expected}")
    except Exception as e:
        print(f"ERROR: Exercise 4 - {e}")
        
    # Test 5
    try:
        if is_stateful_candidate("Patient Chart") is True and is_stateful_candidate("BMI Calculator") is False:
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5 - Logic check failed")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        rx = create_prescription("Aspirin", "100mg", "Daily")
        if rx['drug'] == "Aspirin" and rx['status'] == "Active":
            discontinue_prescription(rx)
            if rx['status'] == "Discontinued":
                print("PASS: Exercise 6")
                passed += 1
            else:
                print("FAIL: Exercise 6 - Status not updated to Discontinued")
        else:
            print("FAIL: Exercise 6 - Creation failed")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
