"""
Unit 2.2: Why Object-Oriented Programming? - Exercises
Focus: Strategic benefits (Modularity, Reusability, Maintainability) and Paradigm selection.
"""

# ============================================================================
# Exercise 1: Identifying the Pillar
# ============================================================================
# CONTEXT: You are a Lead Developer at a HealthTech startup. Match the scenario 
# to the primary OOP Pillar it demonstrates.

def match_pillar(scenario_text):
    """
    Scenarios:
    A. "I fixed a bug in the Prescription printing logic, and it was 
        immediately fixed for both Inpatient and Outpatient modules."
    B. "We added a new Cardiology module with 50 new features without 
        touching a single line of the existing Pediatrics code."
    C. "Our team grew from 5 to 50 developers. Because our code is 
        organized into clear objects, people can work simultaneously 
        without breaking each other's work."
        
    Args:
        scenario_text (str): One of "A", "B", or "C"
        
    Returns:
        str: One of "Reusability", "Modularity", "Scalability"
    """
    # TODO: Implement the mapping
    # Hint: A = Reusability, B = Modularity, C = Scalability
    return {"A": "Reusability", "B": "Modularity", "C": "Scalability"}.get(scenario_text, "")

# ============================================================================
# Exercise 2: Selecting the Paradigm
# ============================================================================
# CONTEXT: Choosing the right tool for the job.

def best_paradigm_for(task_description):
    """
    Options: "Procedural", "Functional", "Object-Oriented"
    
    Tasks:
    1. "A 10-line script to rename PDF lab results in a folder."
    2. "A complex Electronic Health Record system with Patients, 
        Doctors, Insurance, and Billing interacting."
    3. "A pure mathematical calculation to determine the probability 
        of a drug interaction based on 10,000 static data points."
        
    Returns:
        str: The best paradigm for the given task.
    """
    if "10-line script" in task_description:
        # TODO: Return "Procedural"
        return "Procedural"
    elif "Electronic Health Record" in task_description:
        # TODO: Return "Object-Oriented"
        return "Object-Oriented"
    elif "mathematical calculation" in task_description:
        # TODO: Return "Functional"
        return "Functional"
    return ""

# ============================================================================
# Exercise 3: The "Ripple Effect" Analysis
# ============================================================================
# CONTEXT: Maintenance is the biggest cost in software.
#
# Scenario: In a procedural system, 'patient_id' format changes from int to str.
# This variable is used in 40 different global functions across 10 files.
#
# MISSION: Determine the "Cost of Change".

def calculate_change_complexity(is_object_oriented):
    """
    In an OO system, 'patient_id' is encapsulated inside a 'Patient' object.
    You only change the internal 'Patient' logic; the rest of the app 
    just calls patient.get_id().
    
    Args:
        is_object_oriented (bool)
        
    Returns:
        int: Estimated 'Points of Failure' (High for False, Low for True)
    """
    # TODO: Return 1 for OO, return 40 for Procedural
    return 1 if is_object_oriented else 40

# ============================================================================
# Exercise 4: Identifying Domain Objects (Healthcare)
# ============================================================================
# CONTEXT: High Cohesion - Grouping things that belong together.

def get_cohesive_group(entity_name):
    """
    If the entity is "Prescription", what data and behavior should stay together?
    
    Args:
        entity_name (str): "Prescription"
        
    Returns:
        list: 3 items that strictly belong to a Prescription object.
    """
    # TODO: Return a list containing: "drug_name", "dosage", "validate_frequency()"
    return ["drug_name", "dosage", "validate_frequency()"]

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.2 Conceptual Exercises...")
    passed = 0
    total = 4

    # Test 1
    if match_pillar("A") == "Reusability" and match_pillar("B") == "Modularity":
        print("PASS: Exercise 1")
        passed += 1
    else:
        print("FAIL: Exercise 1")

    # Test 2
    if "Object-Oriented" in best_paradigm_for("Electronic Health Record"):
        print("PASS: Exercise 2")
        passed += 1
    else:
        print("FAIL: Exercise 2")

    # Test 3
    if calculate_change_complexity(True) == 1 and calculate_change_complexity(False) == 40:
        print("PASS: Exercise 3")
        passed += 1
    else:
        print("FAIL: Exercise 3")

    # Test 4
    p_group = get_cohesive_group("Prescription")
    if "drug_name" in p_group and "validate_frequency()" in p_group:
        print("PASS: Exercise 4")
        passed += 1
    else:
        print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
