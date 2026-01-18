"""
Unit 2.9: Representing Classes in Python - Exercises
"""

# ============================================================================
# Exercise 1: The PEP 8 Auditor
# ============================================================================
# Rename the class and method below to follow PEP 8 standards.

# TODO: Rename 'patientrecord' to 'PatientRecord'
# TODO: Rename 'ADD_VITALS' to 'add_vitals'
class PatientRecord:
    def __init__(self, name):
        self.name = name
    
    def add_vitals(self, hr, bp):
        pass

# ============================================================================
# Exercise 2: The Constructor Mechanic
# ============================================================================
class ClinicalStaff:
    # TODO: Implement __init__ to store name, role, dept, and empid
    def __init__(self, name, role, dept, empid):
        self.name = name
        self.role = role
        self.dept = dept
        self.empid = empid

# ============================================================================
# Exercise 3: Mastering 'self'
# ============================================================================
class HeartMonitor:
    def __init__(self, bpm):
        self.bpm = bpm

    def set_bpm(self, new_bpm):
        # TODO: Fix this line so it updates the instance attribute bpm
        self.bpm = new_bpm 

    def get_status(self):
        # TODO: Fix this line to access the instance attribute bpm
        if self.bpm > 100:
            return "ALARM"
        return "NORMAL"

# ============================================================================
# Exercise 4: Instance Independence
# ============================================================================
class MedicalDevice:
    def __init__(self, serial_num):
        self.serial_num = serial_num

def main():
    # TODO: Create three unique devices (d1, d2, d3) with different serials
    d1 = MedicalDevice("SN001")
    d2 = MedicalDevice("SN002")
    d3 = MedicalDevice("SN003")
    
    # Validation Code (Don't change)
    if d1 and d2 and d3:
        print(f"Devices created: {d1.serial_num}, {d2.serial_num}, {d3.serial_num}")

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.9 Standards Exercises...")
    passed = 0
    
    # Test 1: PEP 8 (Checking naming by looking at locals)
    try:
        if "PatientRecord" in globals() and hasattr(globals()["PatientRecord"], "add_vitals"):
            print("PASS: Exercise 1")
            passed += 1
        else: print("FAIL: Exercise 1")
    except: print("FAIL: Exercise 1")
    
    # Test 2: Constructor
    try:
        staff = ClinicalStaff("Alice", "Nurse", "ER", 101)
        if staff.name == "Alice" and staff.empid == 101:
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Self
    try:
        hm = HeartMonitor(80)
        hm.set_bpm(120)
        if hm.bpm == 120 and hm.get_status() == "ALARM":
            print("PASS: Exercise 3")
            passed += 1
        else: print("FAIL: Exercise 3")
    except: print("FAIL: Exercise 3")

    # Test 4: Independence
    try:
        o1 = MedicalDevice("X")
        o2 = MedicalDevice("Y")
        if o1.serial_num != o2.serial_num:
            print("PASS: Exercise 4")
            passed += 1
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
