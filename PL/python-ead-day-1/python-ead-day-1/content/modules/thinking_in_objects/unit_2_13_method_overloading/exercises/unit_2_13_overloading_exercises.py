"""
Unit 2.13: Method Overloading & Python's Approach - Exercises
"""

# ============================================================================
# Exercise 1: The Adaptive Dosage
# ============================================================================
class DoseAdmin:
    # TODO: Implement prescribe(medicine, dose_mg=10)
    def prescribe(self, medicine, dose_mg=10):
        return f"{medicine}: {dose_mg}mg"

# ============================================================================
# Exercise 2: The Vital Aggregator
# ============================================================================
class HealthLog:
    # TODO: Implement record_bp(*readings) to return average
    def record_bp(self, *readings):
        return sum(readings) // len(readings)

# ============================================================================
# Exercise 3: The Meta-Patient Record
# ============================================================================
class PatientRecord:
    def __init__(self):
        self.metadata = {}

    # TODO: Implement update(**kwargs) to populate self.metadata
    def update(self, **kwargs):
        self.metadata.update(kwargs)

# ============================================================================
# Exercise 4: Logic Branching
# ============================================================================
class Finder:
    # TODO: Implement search(query)
    # If query is int: return "Searching by ID"
    # If query is str: return "Searching by Name"
    def search(self, query):
        return "Searching by ID" if isinstance(query, int) else "Searching by Name"

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.13 Overloading Exercises...")
    passed = 0
    
    # Test 1: Defaults
    try:
        da = DoseAdmin()
        if da.prescribe("Aspirin") == "Aspirin: 10mg" and da.prescribe("Aspirin", 50) == "Aspirin: 50mg":
            print("PASS: Exercise 1")
            passed += 1
    except: print("FAIL: Exercise 1")
    
    # Test 2: *args
    try:
        log = HealthLog()
        avg = log.record_bp(120, 130, 140)
        if avg == 130:
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: **kwargs
    try:
        pr = PatientRecord()
        pr.update(gender="M", smoking=True)
        if pr.metadata.get("gender") == "M" and pr.metadata.get("smoking") == True:
            print("PASS: Exercise 3")
            passed += 1
    except: print("FAIL: Exercise 3")

    # Test 4: Type Checking
    try:
        f = Finder()
        if f.search(101) == "Searching by ID" and f.search("Alice") == "Searching by Name":
            print("PASS: Exercise 4")
            passed += 1
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
