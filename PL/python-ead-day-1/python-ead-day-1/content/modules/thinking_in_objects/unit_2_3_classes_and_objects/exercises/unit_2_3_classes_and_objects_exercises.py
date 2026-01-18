"""
Unit 2.3: Classes and Objects - Exercises
"""

# ============================================================================
# Exercise 1: The Doctor Blueprint
# ============================================================================
# TODO: Define a class named 'Doctor'
# 1. Use def __init__(self, name, specialty) to set state
# 2. Store name in self.name and specialty in self.specialty

class Doctor:
    def __init__(self, name, specialty):
        # TODO: Implement
        self.name = name
        self.specialty = specialty
    
    def introduce(self):
        return f"Hi, I'm {self.name}, a {self.specialty} expert."

# ============================================================================
# Exercise 2: State vs. Identity
# ============================================================================
def test_identity():
    """
    Create two doctor objects for 'Dr. Smith' (Cardiology).
    Prove they have different IDs.
    """
    # TODO: Create dr1 and dr2
    dr1 = Doctor("Dr. Smith", "Cardiology")
    dr2 = Doctor("Dr. Smith", "Cardiology")
    # TODO: Return True if id(dr1) != id(dr2)
    return id(dr1) != id(dr2)

# ============================================================================
# Exercise 3: Adding Behavior
# ============================================================================
# TODO: Update the Doctor class above (or redefine here) to add a method:
# 'introduce(self)' that returns "Hi, I'm [name], a [specialty] expert."

def check_intro():
    # TODO: Create a doctor and return the result of introduce()
    d = Doctor("Test", "Surgery")
    return d.introduce()

# ============================================================================
# Exercise 4: The Patient Lifecycle (Updating State)
# ============================================================================
# TODO: Define a class 'Patient'
# 1. __init__: sets self.name and self.status (default "Treatment")
# 2. discharge(self): changes self.status to "Discharged"

class Patient:
    # TODO: Implement
    def __init__(self, name, status="Treatment"):
        self.name = name
        self.status = status
    
    def discharge(self):
        self.status = "Discharged"

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.3 Classes & Objects Exercises...")
    passed = 0
    total = 4

    # Test 1: Class Existence
    try:
        d = Doctor("House", "Diagnostics")
        if d.name == "House":
            print("PASS: Exercise 1")
            passed += 1
    except: print("FAIL: Exercise 1")

    # Test 2: Identity
    if test_identity():
        print("PASS: Exercise 2")
        passed += 1
    else: print("FAIL: Exercise 2")

    # Test 3: Behavior
    try:
        intro = check_intro()
        if "expert" in intro:
            print("PASS: Exercise 3")
            passed += 1
        else: print("FAIL: Exercise 3")
    except: print("FAIL: Exercise 3")

    # Test 4: Mutation
    try:
        p = Patient("Alice")
        p.discharge()
        if p.status == "Discharged":
            print("PASS: Exercise 4")
            passed += 1
        else: print("FAIL: Exercise 4")
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
