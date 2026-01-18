"""
Unit 2.10: Access Control & Encapsulation - Exercises
"""

# ============================================================================
# Exercise 1: Naming Signals
# ============================================================================
class Patient:
    def __init__(self, name, internal_id, ssn):
        # TODO: Assign using public, protected (_), and private (__) 
        self.name = name
        self._internal_id = internal_id
        self.__ssn = ssn

# ============================================================================
# Exercise 2: The Read-Only Property
# ============================================================================
class HeartRate:
    def __init__(self, value):
        self._value = value

    # TODO: Implement a read-only property 'bpm'
    @property
    def bpm(self):
        return self._value

# ============================================================================
# Exercise 3: The Validating Setter
# ============================================================================
class BloodSugar:
    def __init__(self, level):
        self._level = level

    # TODO: Implement getter for level
    @property
    def level(self):
        return self._level
    
    # TODO: Implement setter for level (range: 0 to 1000)
    @level.setter
    def level(self, value):
        if 0 <= value <= 1000:
            self._level = value

# ============================================================================
# Exercise 4: Handing Mangled Names
# ============================================================================
class SecureRecord:
    def __init__(self):
        self.__key = "SECRET-123"

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.10 Encapsulation Exercises...")
    passed = 0
    
    # Test 1: Naming
    try:
        p = Patient("Alice", "ID1", "SSN1")
        if hasattr(p, "name") and hasattr(p, "_internal_id") and not hasattr(p, "__ssn"):
            print("PASS: Exercise 1")
            passed += 1
        else: print("FAIL: Exercise 1")
    except: print("FAIL: Exercise 1")
    
    # Test 2: Read-only
    try:
        hr = HeartRate(75)
        val = hr.bpm
        hr.bpm = 80 # Should fail since no setter
        print("FAIL: Exercise 2")
    except AttributeError:
        print("PASS: Exercise 2")
        passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Validation
    try:
        bs = BloodSugar(100)
        bs.level = 200
        bs.level = -50 # Should be rejected
        if bs.level == 200:
            print("PASS: Exercise 3")
            passed += 1
        else: print("FAIL: Exercise 3")
    except: print("FAIL: Exercise 3")

    # Test 4: Mangling Access
    try:
        rec = SecureRecord()
        # TODO: Access the __key from rec using mangling
        mangled_key = rec._SecureRecord__key
        if mangled_key == "SECRET-123":
            print("PASS: Exercise 4")
            passed += 1
        else: print("FAIL: Exercise 4")
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
