"""
Unit 2.16: Putting It All Together - Exercises
"""

# ============================================================================
# Exercise 1: Refactoring "The Script"
# ============================================================================
# TARGET: Convert this procedural mess into an InventoryManager class
inventory_db = {}

def add_inv_item(name, qty):
    if name in inventory_db:
        inventory_db[name] += qty
    else:
        inventory_db[name] = qty

def get_inv_qty(name):
    return inventory_db.get(name, 0)

# TODO: Implement InventoryManager class
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    
    def add_item(self, name, qty):
        if name in self.inventory:
            self.inventory[name] += qty
        else:
            self.inventory[name] = qty
    
    def get_qty(self, name):
        return self.inventory.get(name, 0)

# ============================================================================
# Exercise 2: The God Object Fix
# ============================================================================
# TARGET: Split this class into AdmissionOffice and Cafeteria
class HospitalSuperSystem:
    def admit_patient(self, name):
        return f"Admitted {name}"
    
    def sell_sandwich(self):
        return "Sold BLT"

# TODO: Define AdmissionOffice
class AdmissionOffice:
    def admit_patient(self, name):
        return f"Admitted {name}"

# TODO: Define Cafeteria
class Cafeteria:
    def sell_sandwich(self):
        return "Sold BLT"

# ============================================================================
# Exercise 3: The Data Clump
# ============================================================================
# TARGET: Refactor create_appt to take objects instead of primitives
class Doctor:
    def __init__(self, name): self.name = name

class Patient:
    def __init__(self, name): self.name = name

class Scheduler:
    # BAD METHOD: def create_appt(self, d_name, d_spec, p_name, p_age): ...
    
    # TODO: Implement create_appointment(self, doctor, patient)
    def create_appointment(self, doctor, patient):
        return f"Appointment: {doctor.name} with {patient.name}"

# ============================================================================
# Exercise 4: Full Flow Integration
# ============================================================================
class Donor:
    def __init__(self, weight, iron_level):
        self.weight = weight
        self.iron_level = iron_level

# TODO: Implement BloodBank
# - method donate(donor): returns True if weight > 50 and iron > 12, else False
class BloodBank:
    def donate(self, donor):
        return donor.weight > 50 and donor.iron_level > 12

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.16 Capstone Exercises...")
    passed = 0
    
    # Test 1: Inventory
    try:
        im = InventoryManager()
        im.add_item("Swab", 100)
        im.add_item("Swab", 50)
        if im.get_qty("Swab") == 150:
            print("PASS: Exercise 1")
            passed += 1
    except: print("FAIL: Exercise 1")

    # Test 2: God Object
    try:
        ao = AdmissionOffice()
        caf = Cafeteria()
        if hasattr(ao, 'admit_patient') and not hasattr(ao, 'sell_sandwich'):
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Data Clump
    try:
        s = Scheduler()
        d = Doctor("Dr. A")
        p = Patient("Bob")
        if "Dr. A with Bob" in s.create_appointment(d, p):
            print("PASS: Exercise 3")
            passed += 1
    except: print("FAIL: Exercise 3")

    # Test 4: Logic
    try:
        bb = BloodBank()
        d1 = Donor(60, 14) # Good
        d2 = Donor(40, 10) # Bad
        if bb.donate(d1) == True and bb.donate(d2) == False:
            print("PASS: Exercise 4")
            passed += 1
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
