# Lab 3 Tasks: Hospital Registry System

## Task 1: Incorporate a Class Variable
**Difficulty**: Easy | **Points**: 15

### Objective
Store shared data at the class level.

### Requirements
- Update the `Patient` class.
- Define a class variable `clinic_name` and set it to `"St. Mary Hospital"`.
- This variable MUST be outside any method.

---

## Task 2: Create the HospitalRegistry Class
**Difficulty**: Intermediate | **Points**: 35

### Objective
Create a manager class for collections of patients.

### Requirements
- Define a new class `HospitalRegistry`.
- Its `__init__` should initialize an empty list named `self.patients`.
- Create a method `register_patient(self, patient_obj)`.
  - It should append the `Patient` instance to the `self.patients` list.

---

## Task 3: Implement search functionality
**Difficulty**: Advanced | **Points**: 35

### Objective
Retrieve specific objects from a collection.

### Requirements
- In `HospitalRegistry`, create a method `get_patient(self, patient_id)`.
- It should iterate through the `self.patients` list.
- If a patient with the matching `patient_id` is found, return that entire object.
- If no match is found, return `None`.

---

## Task 4: Global Updates & Identity
**Difficulty**: Advanced | **Points**: 15

### Objective
Demonstrate the power of class variables and memory references.

### Requirements
- In the `if __name__ == "__main__":` block:
- Create 2 patients.
- Change `Patient.clinic_name` to `"Global Care Unit"`.
- Verify that both patients now report the new clinic name.
- Compare the two patients using `is` and print the result.
