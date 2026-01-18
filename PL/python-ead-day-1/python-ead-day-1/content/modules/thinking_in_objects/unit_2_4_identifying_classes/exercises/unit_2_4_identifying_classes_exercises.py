"""
Unit 2.4: Identifying Classes – Analysis & Modelling
"""

# ============================================================================
# Exercise 1: The Noun-Verb Extractor
# ============================================================================
# Scenario: 
# "The Pharmacist uses the PharmacyUI to enter a Prescription for a Patient. 
# The system must check for Drug Interactions before printing the Label."

# TODO: Fill in the lists below based on the scenario.
# Use Python strings.

# Nouns that should be CLASSES
CLINICAL_CLASSES = [
    "Pharmacist",
    # TODO: Add 3-4 more
    "PharmacyUI",
    "Prescription",
    "Patient",
    "Drug",
    "Label"
]

# Verbs that should be METHODS
CLINICAL_METHODS = [
    "enter",
    # TODO: Add 2-3 more
    "check",
    "print"
]

# ============================================================================
# Exercise 2: The BCE Classifier
# ============================================================================
# Categorize the following: 
# Patient, LabResult, AdmissionForm(UI), TriageLogic, HL7ExternalInterface, EHRDatabase

BCE_MAPPING = {
    "ENTITY": ["Patient", "LabResult"],    # Stable data objects
    "BOUNDARY": ["AdmissionForm", "HL7ExternalInterface", "EHRDatabase"],  # High-change I/O or Interfaces
    "CONTROL": ["TriageLogic"]    # Logic/Processing engines
}

# TODO: Distribute the 6 items above into the lists in BCE_MAPPING.

# ============================================================================
# Exercise 3: Spotting the God Object
# ============================================================================
# Consider this class:
"""
class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.staff = []
        self.tax_rates = {}
        self.beds = []
    
    def calculate_surgery_cost(self): pass
    def print_patient_wristband(self): pass
    def check_drug_expiry(self): pass
    def backup_database(self): pass
"""

# TODO: Which of these is the BEST reason why HospitalSystem is a 'God Object'?
# A) It has too many variables.
# B) It lacks 'Single Responsibility' (mixing billing, clinical, and infra logic).
# C) It doesn't have an __init__ method.
GOD_OBJECT_REASON = "B" # Put "A", "B", or "C"

# ============================================================================
# Exercise 4: Attribute or Class?
# ============================================================================
# Requirement: "We need to track the Patient's Address."
# If Address is just a string "123 Main St", it's an ATTRIBUTE.
# If Address has "Street", "City", "Zip", and "Validation Logic", it should be a CLASS.

# Based on industrial standards (HL7/FHIR), should 'Address' be:
# 1. Attribute
# 2. Class
ADDRESS_DECISION = 2 # Put 1 or 2

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.4 Analysis Exercises...")
    passed = 0
    
    # Test 1
    if "Prescription" in CLINICAL_CLASSES and "check" in CLINICAL_METHODS:
        print("PASS: Exercise 1")
        passed += 1
    else: print("FAIL: Exercise 1")
    
    # Test 2
    try:
        if "Patient" in BCE_MAPPING["ENTITY"] and "AdmissionForm" in BCE_MAPPING["BOUNDARY"]:
            print("PASS: Exercise 2")
            passed += 1
        else: print("FAIL: Exercise 2")
    except: print("FAIL: Exercise 2")

    # Test 3
    if GOD_OBJECT_REASON == "B":
        print("PASS: Exercise 3")
        passed += 1
    else: print("FAIL: Exercise 3")

    # Test 4
    if ADDRESS_DECISION == 2:
        print("PASS: Exercise 4")
        passed += 1
    else: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
