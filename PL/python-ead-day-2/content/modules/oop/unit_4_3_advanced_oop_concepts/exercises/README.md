# Unit 4.3: Advanced OOP Concepts - Exercises

## Overview
This unit covers advanced object-oriented programming techniques in Python. These exercises will help you master class composition, mixins, dataclasses, memory optimization with `__slots__`, and the basics of metaclasses.

**File**: `unit_4_3_advanced_oop_concepts_exercises.py`

---

## Exercise List

### Exercise 1: Basic Composition (Car and Engine)
**Description**: Demonstrate the "Has-A" relationship by creating an `Engine` class and a `Car` class that contains an instance of `Engine`.
- **Inputs**: Engine type (str), horsepower (int).
- **Outputs**: String description of the car and its engine.
- **Requirements**:
  - `Engine` class with `engine_type` and `horsepower`.
  - `Car` class with `make`, `model`, and an `engine` attribute.
  - `Car.start()` method that calls `self.engine.ignite()`.
- **Hints**:
  - Hint 1: Don't inherit. Pass the engine instance to the Car's `__init__`.
  - Hint 2: Composition means one object is an attribute of another.
  - See Solution: `self.engine = engine`

---

### Exercise 2: Class Composition - Healthcare (Patient History)
**Description**: Model a patient's medical history by composing a `Patient` class with a list of `VitalReading` objects.
- **Inputs**: List of tuples (heart_rate, blood_pressure).
- **Outputs**: Average heart rate.
- **Requirements**:
  - `VitalReading` class with `heart_rate` and `bp`.
  - `Patient` class with a `history` list attribute.
  - Method `Patient.add_reading()` and `Patient.get_average_heart_rate()`.
- **Hints**:
  - Hint 1: The `history` list should hold instances of `VitalReading`.
  - Hint 2: Sum the heart rates and divide by `len(history)`.

---

### Exercise 3: JSON Export Mixin
**Description**: Create a Mixin class that adds JSON serialization functionality to any class it is inherited by.
- **Inputs**: Object attributes.
- **Outputs**: JSON string.
- **Requirements**:
  - `JSONMixin` class with a `to_json()` method using the `json` module.
  - `to_json` should use `self.__dict__`.
  - Apply to a `Product` class.
- **Hints**:
  - Hint 1: Inherit from `JSONMixin` alongside other classes.
  - Hint 2: Use `json.dumps(self.__dict__)`.

---

### Exercise 4: Multiple Mixins (Logging and Validation)
**Description**: Combine multiple mixins into a single class to provide modular functionality.
- **Inputs**: User data.
- **Outputs**: Log messages and validation result.
- **Requirements**:
  - `LogMixin` with `log(msg)`.
  - `ValidationMixin` with `validate(data)`.
  - `UserAccount` inheriting from both.

---

### Exercise 5: Basic Dataclass (Employee)
**Description**: Use the `@dataclass` decorator to create a simple data container.
- **Inputs**: name, id, department.
- **Outputs**: Auto-generated `repr` string.
- **Requirements**:
  - Import `dataclass` from `dataclasses`.
  - Create `Employee` with type hints.
- **Hints**:
  - Hint 1: Remember the type hints are mandatory for dataclasses.

---

### Exercise 6: Frozen Dataclass (Coordinates)
**Description**: Create an immutable (frozen) dataclass to represent static data.
- **Inputs**: lat, lon.
- **Outputs**: `FrozenInstanceError` when attempting to modify.
- **Requirements**:
  - `@dataclass(frozen=True)`.

---

### Exercise 7: Dataclass Default Factory (Medical Record)
**Description**: Use `field(default_factory=list)` to initialize a list in a dataclass correctly.
- **Inputs**: Patient name.
- **Outputs**: Empty list by default.
- **Requirements**:
  - `PatientRecord` dataclass.
  - `medications` list field with `default_factory`.

---

### Exercise 8: Memory Optimization with `__slots__`
**Description**: Use `__slots__` to limit attribute creation and save memory.
- **Requirements**:
  - `CompactPoint` class with `__slots__ = ('x', 'y')`.
  - Attempt to add attribute `z` and catch the exception.
- **Hints**:
  - Hint 1: `__slots__` should be a tuple of strings.

---

### Exercise 9: Basic Metaclass (Enforced Attributes)
**Description**: Create a metaclass that ensures all new classes have a specific attribute defined.
- **Requirements**:
  - `RegistryMeta` metaclass.
  - It should check if `REQUIRED_VERSION` is in the class attributes.
  - Raise `TypeError` if missing.
- **Hints**:
  - Hint 1: Override the `__new__` method of the metaclass.

---

### Exercise 10: Advanced Composition (Hospital Ward)
**Description**: Build a system where a `HospitalWard` is composed of `Doctor` and `Patient` objects (both Dataclasses) and uses a `LogMixin`.
- **Requirements**:
  - Use Dataclasses for `Doctor` and `Patient`.
  - `HospitalWard` class with lists for both.
  - Use a mixin for logging ward events.
