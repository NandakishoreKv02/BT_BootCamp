"""
Unit 2.5: Attributes and Methods - Exercises
"""

# ============================================================================
# Exercise 1: Unique IDs vs. Shared Clinic Name
# ============================================================================
class Patient:
    # TODO: Define a CLASS ATTRIBUTE named 'clinic' set to "Apollo Health"
    clinic = "Apollo Health"
    
    def __init__(self, name, mrn):
        # TODO: Define INSTANCE ATTRIBUTES for name and mrn
        self.name = name
        self.mrn = mrn

# ============================================================================
# Exercise 2: The Signature Architect
# ============================================================================
class Prescription:
    def __init__(self, drug):
        self.drug = drug
        self.dose = 0
        self.unit = "mg"

    # TODO: Define an instance method 'set_dose'
    # Requirements: 
    # 1. Take 'amount' and 'unit_type' as arguments
    # 2. Update self.dose and self.unit
    # 3. Return a string: "Dose updated to [amount][unit_type]"
    def set_dose(self, amount, unit_type):
        self.dose = amount
        self.unit = unit_type
        return f"Dose updated to {amount}{unit_type}"

# ============================================================================
# Exercise 3: The Global Admissions Counter
# ============================================================================
class HospitalAdmission:
    # TODO: Define a CLASS ATTRIBUTE 'total_count' initialized to 0
    total_count = 0
    
    def __init__(self, patient_name):
        self.patient_name = patient_name
        # TODO: Increment the CLASS ATTRIBUTE 'total_count' by 1 every time
        # a new admission is created. (Hint: Use HospitalAdmission.total_count)
        HospitalAdmission.total_count += 1

# ============================================================================
# Exercise 4: Cohesion Audit
# ============================================================================
# Look at the methods in the class below:
class BloodWork:
    def __init__(self, lab_id):
        self.lab_id = lab_id

    def run_analysis(self): pass
    def print_vials_label(self): pass
    def calculate_employee_payroll(self): pass # <-- Is this cohesive?
    def generate_results_summary(self): pass

# TODO: Assign the name of the method that has LOW COHESION to the variable below:
UNCLEAN_METHOD_NAME = "calculate_employee_payroll"

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.5 Attributes & Methods Exercises...")
    passed = 0
    
    # Test 1: Class vs Instance
    try:
        p1 = Patient("Alice", "MRN1")
        p2 = Patient("Bob", "MRN2")
        if p1.clinic == p2.clinic and p1.mrn != p2.mrn:
            print("PASS: Exercise 1")
            passed += 1
    except: print("FAIL: Exercise 1")

    # Test 2: Signatures
    try:
        rx = Prescription("Insulin")
        msg = rx.set_dose(10, "units")
        if rx.dose == 10 and "10units" in msg:
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Counters
    try:
        # Reset if needed
        HospitalAdmission.total_count = 0
        h1 = HospitalAdmission("A")
        h2 = HospitalAdmission("B")
        if HospitalAdmission.total_count == 2:
            print("PASS: Exercise 3")
            passed += 1
    except: print("FAIL: Exercise 3")

    # Test 4: Cohesion
    if "payroll" in UNCLEAN_METHOD_NAME.lower():
        print("PASS: Exercise 4")
        passed += 1
    else: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
