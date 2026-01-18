"""
Unit 2.8: Modelling Exercises – Real-World Scenarios
"""

# ============================================================================
# Exercise 1: Identification
# ============================================================================
# Requirements: "A Pharmacist checks a Prescription. If valid, they Dispense
# the Medication from the Inventory."

# TODO: Classify the following as "CLASS" or "METHOD"
ANALYSIS = {
    "Pharmacist": "CLASS",
    "check_validity": "METHOD",
    "Prescription": "CLASS",
    "Dispense": "METHOD",
    "Inventory": "CLASS"
}

# ============================================================================
# Exercise 2: The Is-a vs Has-a Decision
# ============================================================================
# Scenario: Every 'Surgeon' is a 'Physician'. Every 'Surgeon' has a 'Bleeper'.

class Physician:
    def __init__(self, name): self.name = name

class Bleeper:
    def __init__(self, frequency): self.frequency = frequency

# TODO: Implement Surgeon using the correct relationships
class Surgeon(Physician):
    def __init__(self, name, frequency):
        super().__init__(name)
        self.bleeper = Bleeper(frequency)

# ============================================================================
# Exercise 3: Multiplicity Modelling
# ============================================================================
# Scenario: A 'Clinic' has many 'ExamRooms' (Composition). 
# A 'Clinic' manages many 'Nurses' (Aggregation).

class ExamRoom:
    def __init__(self, room_id): self.room_id = room_id

class Nurse:
    def __init__(self, name): self.name = name

class Clinic:
    def __init__(self, name, room_count):
        self.name = name
        # TODO: Implement 1:N Composition for ExamRooms (Create 'room_count' rooms)
        self.rooms = [ExamRoom(i) for i in range(room_count)]
        # TODO: Initialize 1:N Aggregation for Nurses
        self.staff = []

    def hire_nurse(self, nurse_obj):
        # TODO: Add nurse to staff
        self.staff.append(nurse_obj)

# ============================================================================
# Exercise 4: Refinement (Splitting the God Object)
# ============================================================================
# The following class is too big (Low Cohesion). 
# Split it into 'Inventory' and 'PatientRecord'.

class OldMessyHospital:
    def __init__(self):
        self.medications = [] # Inventory data
        self.patient_names = [] # Record data
        self.patient_bills = [] # Record data

class Inventory:
    # TODO: Implement with 'medications'
    def __init__(self):
        self.medications = []

class PatientRecord:
    # TODO: Implement with 'names' and 'bills'
    def __init__(self):
        self.patient_names = []
        self.patient_bills = []

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.8 Modelling Exercises...")
    passed = 0
    
    # Test 1: Identification
    if ANALYSIS["Pharmacist"] == "CLASS" and ANALYSIS["check_validity"] == "METHOD":
        print("PASS: Exercise 1")
        passed += 1
    else: print("FAIL: Exercise 1")
    
    # Test 2: Relationships
    try:
        s = Surgeon("Dr. Grey", 99.5)
        if isinstance(s, Physician) and isinstance(s.bleeper, Bleeper):
            print("PASS: Exercise 2")
            passed += 1
        else: print("FAIL: Exercise 2")
    except: print("FAIL: Exercise 2")

    # Test 3: Multiplicity
    try:
        c = Clinic("Family Care", 4)
        n = Nurse("Joy")
        c.hire_nurse(n)
        if len(c.rooms) == 4 and n in c.staff:
            print("PASS: Exercise 3")
            passed += 1
        else: print("FAIL: Exercise 3")
    except: print("FAIL: Exercise 3")

    # Test 4: Refinement
    try:
        inv = Inventory(); rec = PatientRecord()
        if hasattr(inv, 'medications') and hasattr(rec, 'patient_names'):
            print("PASS: Exercise 4")
            passed += 1
        else: print("FAIL: Exercise 4")
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
