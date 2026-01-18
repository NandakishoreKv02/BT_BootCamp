# Lab 7 Tasks: Integrated Clinic Record

## Task 1: Complex Object Initialization
**Difficulty**: Expert | **Points**: 100

### Objective
Store compound data structures within an object.

### Requirements
- Create a `Patient` class.
- Add a class variable `facility_code` set to "GEN-HOSP".
- The `__init__` method should take `name`.
- Inside `__init__`:
    1. Store `self.name`.
    2. Initialize `self.contacts` as an empty list.
    3. Initialize `self.medications` as an empty list.
    4. Initialize `self.vitals` as a dictionary containing: `{"temp": 0.0, "hr": 0}`.
- Prove you can add a medication like "Aspirin" to the instance list.
