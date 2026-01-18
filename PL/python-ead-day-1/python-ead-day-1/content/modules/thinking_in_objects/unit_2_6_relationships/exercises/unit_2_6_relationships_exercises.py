"""
Unit 2.6: Relationships Between Classes - Exercises
"""

# ============================================================================
# Exercise 1: The Relationship Classifier
# ============================================================================
# Identify the relationship for each pair: 
# "IS-A", "HAS-A", or "USES"

RELATIONSHIPS = {
    "Nurse/Person": "IS-A",               # e.g. "IS-A"
    "Hospital/EmergencyRoom": "HAS-A",     # e.g. "HAS-A"
    "Doctor/Stethoscope": "USES",          # e.g. "USES" or "HAS-A"
    "Patient/InsuranceClaim": "USES"       # e.g. "USES"
}

# TODO: Fill in the values above with "IS-A", "HAS-A", or "USES"

# ============================================================================
# Exercise 2: Composition vs. Aggregation (Has-a)
# ============================================================================
class MedicalRecord:
    def __init__(self, mrn):
        self.mrn = mrn

class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name, mrn, primary_doctor=None):
        self.name = name
        # TODO: Implement COMPOSITION (Strong Has-a)
        # Create a MedicalRecord object inside __init__ and assign to self.record
        self.record = MedicalRecord(mrn)
        
        # TODO: Implement AGGREGATION (Weak Has-a / Association)
        # Assign the passed primary_doctor object to self.doctor
        self.doctor = primary_doctor

# ============================================================================
# Exercise 3: The Dependency Injector (Uses)
# ============================================================================
class ClinicalAnalyst:
    # This class owns NO data. It just processes other objects.
    
    # TODO: Define a method 'summarize'
    # 1. Take a 'patient_obj' as a parameter (USES relationship)
    # 2. Return a string: "Analyzing [name] with MRN [mrn]"
    def summarize(self, patient_obj):
        return f"Analyzing {patient_obj.name} with MRN {patient_obj.record.mrn}"

# ============================================================================
# Exercise 4: Spotting Modeling Mistakes
# ============================================================================
# Scenario: A developer made 'class Patient(HeartRateMonitor):'
# TODO: What is the BEST reason why this is a mistake?
# A) It's hard to type.
# B) A Patient IS NOT a Monitor; they should HAVE a monitor (Composition) or USE one (Dependency).
# C) Inheritance only works for People.

INHERITANCE_MISTAKE_REASON = "B" # Put "A", "B", or "C"

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.6 Relationship Exercises...")
    passed = 0
    
    # Test 1: Classifier
    if RELATIONSHIPS["Nurse/Person"] == "IS-A" and RELATIONSHIPS["Hospital/EmergencyRoom"] == "HAS-A":
        print("PASS: Exercise 1")
        passed += 1
    else: print("FAIL: Exercise 1")
    
    # Test 2: Composition
    try:
        dr = Doctor("House")
        p = Patient("John", "ABC", dr)
        if isinstance(p.record, MedicalRecord) and p.doctor == dr:
            print("PASS: Exercise 2")
            passed += 1
        else: print("FAIL: Exercise 2")
    except: print("FAIL: Exercise 2")

    # Test 3: Dependency
    try:
        p = Patient("Tony", "123", None)
        p.record = MedicalRecord("MRN-99") # Manual override for test
        analyst = ClinicalAnalyst()
        result = analyst.summarize(p)
        if "Tony" in result and "MRN-99" in result:
            print("PASS: Exercise 3")
            passed += 1
        else: print("FAIL: Exercise 3")
    except: print("FAIL: Exercise 3")

    # Test 4: Mistakes
    if INHERITANCE_MISTAKE_REASON == "B":
        print("PASS: Exercise 4")
        passed += 1
    else: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
