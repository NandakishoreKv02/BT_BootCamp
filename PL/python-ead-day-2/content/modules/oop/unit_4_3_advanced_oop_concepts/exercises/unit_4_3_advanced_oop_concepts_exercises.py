"""
Unit 4.3: Advanced OOP Concepts - Exercises
Practice class composition, mixins, dataclasses, __slots__, and metaclasses.
"""

import json
from dataclasses import dataclass, field

# ============================================================================
# Exercise 1: Basic Composition (Car and Engine)
# ============================================================================

class Engine:
    def __init__(self, engine_type: str, horsepower: int):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def ignite(self):
        return f"{self.engine_type} engine with {self.horsepower} HP is running."

class Car:
    """
    TODO: Implement the Car class using composition.
    Attributes:
        make (str)
        model (str)
        engine (Engine instance)
    Methods:
        start(): Should call self.engine.ignite() and return the string.
    """
    def __init__(self, make: str, model: str, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        return self.engine.ignite()


# ============================================================================
# Exercise 2: Class Composition - Healthcare (Patient History)
# ============================================================================

class VitalReading:
    def __init__(self, heart_rate: int, bp: str):
        self.heart_rate = heart_rate
        self.bp = bp

class Patient:
    """
    TODO: Implement the Patient class using composition with VitalReading.
    Attributes:
        name (str)
        history (list of VitalReading instances)
    Methods:
        add_reading(hr, bp): Adds a new VitalReading to history.
        get_average_heart_rate(): Returns float average or 0 if empty.
    """
    def __init__(self, name: str):
        self.name = name
        self.history = []

    def add_reading(self, heart_rate: int, bp: str):
        self.history.append(VitalReading(heart_rate, bp))

    def get_average_heart_rate(self) -> float:
        if not self.history:
            return 0.0
        return sum(r.heart_rate for r in self.history) / len(self.history)


# ============================================================================
# Exercise 3: JSON Export Mixin
# ============================================================================

class JSONMixin:
    """
    TODO: Implement a mixin that adds JSON serialization.
    Methods:
        to_json(): Returns JSON string representation of instance __dict__.
    """
    def to_json(self):
        return json.dumps(self.__dict__)

class Product(JSONMixin):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


# ============================================================================
# Exercise 4: Multiple Mixins (Logging and Validation)
# ============================================================================

class LogMixin:
    def log(self, message: str):
        return f"[LOG]: {message}"

class ValidationMixin:
    def validate(self, data: dict, required_keys: list):
        return all(key in data for key in required_keys)

class UserAccount(LogMixin, ValidationMixin):
    """
    TODO: Implement a class that uses multiple mixins.
    Attributes:
        username (str)
    Methods:
        create_profile(data): Validates data has ['email', 'age'], 
                             logs "Profile Validated", and returns True/False.
    """
    def __init__(self, username: str):
        self.username = username

    def create_profile(self, data: dict):
        if self.validate(data, ['email', 'age']):
            self.log("Profile Validated")
            return True
        return False


# ============================================================================
# Exercise 5: Basic Dataclass (Employee)
# ============================================================================

# TODO: Create an Employee dataclass with name (str), emp_id (int), and dept (str)
@dataclass
class Employee:
    name: str
    emp_id: int
    dept: str


# ============================================================================
# Exercise 6: Frozen Dataclass (Coordinates)
# ============================================================================

# TODO: Create a frozen Coordinates dataclass with lat (float) and lon (float)
@dataclass(frozen=True)
class Coordinates:
    lat: float
    lon: float


# ============================================================================
# Exercise 7: Dataclass Default Factory (Medical Record)
# ============================================================================

# TODO: Create a PatientRecord dataclass.
# Attributes: patient_name (str), medications (list).
# medications must use default_factory=list.
@dataclass
class PatientRecord:
    patient_name: str
    medications: list = field(default_factory=list)


# ============================================================================
# Exercise 8: Memory Optimization with __slots__
# ============================================================================

class CompactPoint:
    """
    TODO: Use __slots__ to restrict attributes to x and y only.
    """
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


# ============================================================================
# Exercise 9: Basic Metaclass (Enforced Attributes)
# ============================================================================

class RegistryMeta(type):
    """
    TODO: Implement a metaclass that ensures REQUIRED_VERSION is defined in classes.
    """
    def __new__(mcs, name, bases, attrs):
        if name != 'VersionedSystem' and 'REQUIRED_VERSION' not in attrs:
            raise TypeError("Missing REQUIRED_VERSION")
        return super().__new__(mcs, name, bases, attrs)

# TODO: Create a class that uses RegistryMeta
class VersionedSystem(metaclass=RegistryMeta):
    REQUIRED_VERSION = "1.0"


# ============================================================================
# Exercise 10: Advanced Composition (Hospital Ward)
# ============================================================================

@dataclass
class Doctor:
    name: str
    specialty: str

@dataclass
class WardPatient:
    name: str
    condition: str

class HospitalWard(LogMixin):
    """
    TODO: Implement a class composed of Dataclass instances and a Mixin.
    Attributes:
        ward_name (str)
        doctors (list of Doctor)
        patients (list of WardPatient)
    Methods:
        assign_doctor(doctor): Logs assignment and adds to list.
        admit_patient(patient): Logs admission and adds to list.
    """
    def __init__(self, ward_name: str):
        self.ward_name = ward_name
        self.doctors = []
        self.patients = []

    def assign_doctor(self, doctor: Doctor):
        self.log(f"Doctor {doctor.name} assigned")
        self.doctors.append(doctor)

    def admit_patient(self, patient: WardPatient):
        self.log(f"Patient {patient.name} admitted")
        self.patients.append(patient)


# ============================================================================
# Test Cases
# ============================================================================

if __name__ == "__main__":
    print("Running Exercises...")
    
    # Ex 1
    engine = Engine("V8", 500)
    car = Car("Ford", "Mustang", engine)
    try:
        print(f"Ex 1: {car.start()}")
    except:
        print("Ex 1: Not implemented")

    # Ex 2
    p = Patient("John")
    p.add_reading(80, "120/80")
    p.add_reading(90, "130/85")
    print(f"Ex 2: Avg HR: {p.get_average_heart_rate()}")

    # Ex 3
    prod = Product("Mask", 5.99)
    try:
        print(f"Ex 3: {prod.to_json()}")
    except:
        print("Ex 3: Not implemented")

    # Ex 5
    emp = Employee("Alice", 101, "HR")
    print(f"Ex 5: {emp}")

    # Ex 8
    cp = CompactPoint(1, 2)
    try:
        cp.z = 3
        print("Ex 8: FAIL - __slots__ not restricting attributes")
    except AttributeError:
        print("Ex 8: PASS - __slots__ restricting as expected")
    except:
        print("Ex 8: Not implemented")
