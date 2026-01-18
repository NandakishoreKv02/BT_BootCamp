# Lab 1 Tasks: String Representations

## Task 1: Create Patient Class (20 points)
Create a `Patient` class with proper initialization.

**Requirements**:
- Define `__init__` with: patient_id, name, dob, blood_type, admission_date
- Store all attributes as instance variables

## Task 2: Implement `__str__` (30 points)
Create a user-friendly string representation.

**Requirements**:
- Return format: `"Patient: {name} (ID: {patient_id})"`
- Should be clean and readable for medical staff

**Expected Output**:
```python
print(patient)  # Patient: Alice Smith (ID: P001)
```

## Task 3: Implement `__repr__` (30 points)
Create a developer-friendly representation.

**Requirements**:
- Return format: `"Patient('{id}', '{name}', '{dob}', '{blood_type}', '{admission}')"`
- Should show all constructor arguments
- Ideally could be used to recreate the object

**Expected Output**:
```python
repr(patient)  # Patient('P001', 'Alice Smith', '1990-05-15', 'O+', '2024-01-10')
```

## Task 4: Test Both Methods (20 points)
Verify the implementations work correctly.

**Requirements**:
- Create multiple patient instances
- Test print() and repr() on each
- Verify output matches expected format
