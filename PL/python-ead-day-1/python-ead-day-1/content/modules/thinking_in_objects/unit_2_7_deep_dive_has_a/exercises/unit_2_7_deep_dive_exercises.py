"""
Unit 2.7: Has-a Relationships – Deep Dive - Exercises
"""

# ============================================================================
# Exercise 1: One-to-Many Composition
# ============================================================================
class Bed:
    def __init__(self, bed_id):
        self.bed_id = bed_id

class HospitalWard:
    def __init__(self, name, bed_count):
        self.name = name
        # TODO: Implement 1:N COMPOSITION
        # Initialize self.beds as a list. Use a loop to create 'bed_count' 
        # number of Bed objects and add them to the list.
        self.beds = [Bed(i) for i in range(bed_count)]

# ============================================================================
# Exercise 2: Many-to-Many Aggregation
# ============================================================================
class Specialty:
    def __init__(self, name):
        self.name = name

class Doctor:
    def __init__(self, name):
        self.name = name
        # TODO: Initialize self.specialties as an empty list
        self.specialties = []

    def add_specialty(self, specialty_obj):
        # TODO: Add the specialty object to the list (Aggregation)
        self.specialties.append(specialty_obj)

# ============================================================================
# Exercise 3: Lifecycle Ownership
# ============================================================================
class VitalsLog:
    def __init__(self): self.data = []

class InsuranceProvider:
    def __init__(self, name): self.name = name

class Patient:
    def __init__(self, name, provider_obj):
        self.name = name
        # TODO: Implement COMPOSITION for vitals (Create inside __init__)
        self.vitals = VitalsLog()
        
        # TODO: Implement AGGREGATION for provider (Link to passed object)
        self.provider = provider_obj

# ============================================================================
# Exercise 4: Bidirectional Link Sync
# ============================================================================
class Nurse:
    def __init__(self, name):
        self.name = name
        self.station = None

class Station:
    def __init__(self, station_id):
        self.station_id = station_id
        self.nurse_on_duty = None

def assign_nurse_to_station(nurse_obj, station_obj):
    # TODO: Make the nurse point to the station 
    # AND make the station point to the nurse.
    nurse_obj.station = station_obj
    station_obj.nurse_on_duty = nurse_obj

# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 2.7 Deep Dive Exercises...")
    passed = 0
    
    # Test 1: One-to-Many
    try:
        ward = HospitalWard("ICU", 5)
        if len(ward.beds) == 5 and isinstance(ward.beds[0], Bed):
            print("PASS: Exercise 1")
            passed += 1
    except: print("FAIL: Exercise 1")
    
    # Test 2: Many-to-Many
    try:
        dr = Doctor("Strange")
        s1 = Specialty("Surgery")
        s2 = Specialty("Magic")
        dr.add_specialty(s1)
        dr.add_specialty(s2)
        if len(dr.specialties) == 2:
            print("PASS: Exercise 2")
            passed += 1
    except: print("FAIL: Exercise 2")

    # Test 3: Lifecycle
    try:
        prov = InsuranceProvider("MedCare")
        p = Patient("Alice", prov)
        if isinstance(p.vitals, VitalsLog) and p.provider == prov:
            print("PASS: Exercise 3")
            passed += 1
    except: print("FAIL: Exercise 3")

    # Test 4: Bidirectional
    try:
        n = Nurse("Joy")
        s = Station("A1")
        assign_nurse_to_station(n, s)
        if n.station == s and s.nurse_on_duty == n:
            print("PASS: Exercise 4")
            passed += 1
    except: print("FAIL: Exercise 4")

    print(f"\nResult: {passed}/4 tests passed.")

if __name__ == "__main__":
    test_runner()
