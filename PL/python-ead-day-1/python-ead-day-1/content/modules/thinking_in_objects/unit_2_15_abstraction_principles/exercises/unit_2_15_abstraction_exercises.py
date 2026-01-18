"""
Unit 2.15: Abstraction & Design Principles - Exercises
"""
from abc import ABC, abstractmethod

# ============================================================================
# Exercise 1 & 2: Abstract Treatment & Vaccine
# ============================================================================
# TODO: Define abstract class Treatment
class Treatment(ABC):
    @abstractmethod
    def administer(self):
        pass

# TODO: Define concrete class Vaccine inheriting from Treatment
class Vaccine(Treatment):
    def administer(self):
        return "Administering vaccine"

# ============================================================================
# Exercise 3: SRP Refactoring
# ============================================================================
# TARGET CODE TO REFACTOR:
# class PatientManager:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def get_details(self): return self.name
#     def generate_invoice(self): return f"Invoice for {self.name}: {self.balance}"

# TODO: Refactor into Patient and InvoiceGenerator
class Patient:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class InvoiceGenerator:
    def generate(self, patient):
        return f"Invoice for {patient.name}: {patient.balance}"

# ============================================================================
# Exercise 4: Interface Enforcement
# ============================================================================
class LabTest(ABC):
    @abstractmethod
    def get_cost(self):
        pass

# TODO: Implement BloodTest and XRay subclasses
class BloodTest(LabTest):
    def get_cost(self):
        return 50

class XRay(LabTest):
    def get_cost(self):
        return 200

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.15 Abstraction Exercises...")
    passed = 0
    
    # Test 1: ABC Enforcement
    try:
        t = Treatment()
        print("FAIL: Exercise 1 - Treatment should be abstract")
    except TypeError:
        print("PASS: Exercise 1")
        passed += 1
    except: print("FAIL: Exercise 1 - Unexpected Error")

    # Test 2: Concrete Implementation
    try:
        v = Vaccine()
        if hasattr(v, 'administer'):
            print("PASS: Exercise 2")
            passed += 1
        else: print("FAIL: Exercise 2 - administer() missing")
    except: print("FAIL: Exercise 2 - Error")

    # Test 3: SRP
    try:
        p = Patient("Alice", 500)
        ig = InvoiceGenerator()
        if ig.generate(p) == "Invoice for Alice: 500":
            print("PASS: Exercise 3")
            passed += 1
    except: print("FAIL: Exercise 3")

    # Test 4: Interface
    try:
        b = BloodTest()
        x = XRay()
        if b.get_cost() == 50 and x.get_cost() == 200:
            print("PASS: Exercise 4")
            passed += 1
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
