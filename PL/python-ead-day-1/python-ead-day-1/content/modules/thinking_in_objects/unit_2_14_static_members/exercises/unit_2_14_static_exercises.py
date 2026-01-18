"""
Unit 2.14: Static Members & Utility Behavior - Exercises
"""

# ============================================================================
# Exercise 1: The Hospital Population
# ============================================================================
class Patient:
    # TODO: Define static 'population' variable
    population = 0
    
    def __init__(self, name):
        self.name = name
        # TODO: Increment population counter
        Patient.population += 1

# ============================================================================
# Exercise 2: The Dosage Toolkit
# ============================================================================
class MedMath:
    # TODO: Implement @staticmethod to_grams(mg)
    @staticmethod
    def to_grams(mg):
        return mg / 1000

# ============================================================================
# Exercise 3: The Dictionary Intake (Factory Method)
# ============================================================================
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    # TODO: Implement @classmethod from_dict(cls, data)
    # data will be like {'name': 'Alice', 'role': 'Nurse'}
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['role'])

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.14 Static Member Exercises...")
    passed = 0
    
    # Test 1: Static Variable
    try:
        p1 = Patient("A")
        p2 = Patient("B")
        if Patient.population == 2:
            print("PASS: Exercise 1")
            passed += 1
        else: print(f"FAIL: Exercise 1 (Got {Patient.population})")
    except: print("FAIL: Exercise 1 (Error)")
    
    # Test 2: Static Method
    try:
        if MedMath.to_grams(500) == 0.5:
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Class Method Factory
    try:
        s = Staff.from_dict({'name': 'Alice', 'role': 'Nurse'})
        if s.name == "Alice" and isinstance(s, Staff):
            print("PASS: Exercise 3")
            passed += 1
    except: print("FAIL: Exercise 3")

    print(f"\nResult: {passed}/3 tests passed.")

if __name__ == "__main__":
    test_runner()
