"""
Unit 2.11: Constructors & Object Lifecycle - Exercises
"""

# ============================================================================
# Exercise 1: The Flexible Admission
# ============================================================================
class PatientAdmission:
    # TODO: Implement __init__ with a default level of "Standard"
    def __init__(self, patient_name, room_type="Standard"):
        self.patient_name = patient_name
        self.room_type = room_type

# ============================================================================
# Exercise 2: The Optional Consultant
# ============================================================================
class Consultation:
    # TODO: Implement __init__ with optional consultant_name defaulting to None
    def __init__(self, physician_name, consultant_name=None):
        self.physician_name = physician_name
        self.consultant_name = consultant_name

# ============================================================================
# Exercise 3: Avoiding the Shared List Trap
# ============================================================================
class PharmacyOrder:
    # FIX THIS: Currently uses a mutable default which is a bug!
    def __init__(self, order_id, items=None):
        self.order_id = order_id
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)

# ============================================================================
# Exercise 4: Controlled Initialization
# ============================================================================
class IncidentReport:
    # TODO: If severity is 10, set self.is_emergency to True automatically
    def __init__(self, description, severity):
        self.description = description
        self.severity = severity
        self.is_emergency = severity == 10

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.11 Constructor Exercises...")
    passed = 0
    
    # Test 1: Defaults
    try:
        a1 = PatientAdmission("Alice")
        a2 = PatientAdmission("Bob", "VIP")
        if a1.room_type == "Standard" and a2.room_type == "VIP":
            print("PASS: Exercise 1")
            passed += 1
    except: print("FAIL: Exercise 1")
    
    # Test 2: Optional
    try:
        c = Consultation("Dr. Smith")
        if c.consultant_name is None:
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Mutable Trap Check
    try:
        o1 = PharmacyOrder(1)
        o2 = PharmacyOrder(2)
        o1.add_item("Aspirin")
        if len(o2.items) == 0:
            print("PASS: Exercise 3")
            passed += 1
        else:
            print("FAIL: Exercise 3 - Data Leaked between orders!")
    except: print("FAIL: Exercise 3")

    # Test 4: Logic in Constructor
    try:
        r = IncidentReport("Cardiac Arrest", 10)
        if r.is_emergency:
            print("PASS: Exercise 4")
            passed += 1
        else: print("FAIL: Exercise 4")
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
