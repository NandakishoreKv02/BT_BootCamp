# Lab 1 Tasks: Patient Records Management

## Task 1: Create Patient Database
**Difficulty**: Easy
**Points**: 10

### Objective
Initialize the storage structure for patient records.

### Description
In this step, you will define the data structure that holds our patient records. Since we need fast lookups by ID, a dictionary is the ideal choice. You will also create a function to reset/initialize this database.

### Requirements
- Create a function `initialize_database()`
- It should return a dictionary containing at least 2 default "dummy" patients for testing.
- Default patients should have: `id`, `name`, `age`, `blood_type`.

### Example
```python
# Returns:
{
    101: {"name": "John Doe", "age": 30, "blood_type": "A+"},
    102: {"name": "Jane Smith", "age": 25, "blood_type": "O-"}
}
```

### Hints
- Use the integer ID as the key.
- The value should be another dictionary (nested) or just a string details if simplified (for this lab, let's keep it simple: Key=ID, Value=Name for now, or dictionary if you are comfortable. Let's stick to **Key=ID, Value=Name** for this specific Easy lab to focus on dictionary mechanics, or map Key=ID to a dictionary of details. The prompt implies "records", so a nested dict is more realistic but might be intermediate. Let's do **Key=ID, Value=Dictionary of details** as it's standard).
- Wait, "Easy" lab characteristic: "Single responsibility". Nested might be complex. Let's stick to **Key=ID, Value=Dictionary** but simple fields.

---

## Task 2: Add New Patient
**Difficulty**: Easy
**Points**: 15

### Objective
Implement functionality to register a new patient.

### Description
Create a function that takes the patient's details and adds them to the database. You must ensure the ID is unique (dictionaries do this naturally by overwriting, but we want to know if we are overwriting). For this easy lab, we will just add/overwrite.

### Requirements
- Function `add_patient(db, patient_id, name, age, blood_type)`
- Add the patient code to the `db` dictionary.
- Key should be `patient_id`.
- Value should be a dict: `{"name": name, "age": age, "blood_type": blood_type}`.
- Return `True` to indicate success.

### Example
```python
db = {}
add_patient(db, 103, "Sam Brown", 45, "B+")
# db is now {103: {"name": "Sam Brown", "age": 45, "blood_type": "B+"}}
```

---

## Task 3: Safe Patient Lookup
**Difficulty**: Easy
**Points**: 15

### Objective
Retrieve patient details without crashing if the ID doesn't exist.

### Description
The receptionist might type a wrong number. We need a function that looks up a patient and handles "missing" keys gracefully.

### Requirements
- Function `get_patient_details(db, patient_id)`
- Use the `.get()` method.
- If found, return the patient info dictionary.
- If not found, return `None`.

### Hints
- Do not use `db[patient_id]` directly as it raises KeyError.
- `db.get(key)` returns None by default if missing.

---

## Task 4: Update Patient Age
**Difficulty**: Easy
**Points**: 10

### Objective
Modify an existing record.

### Description
Patients get older. We need a way to specificially update just the age of a patient, keeping their name and blood type unchanged.

### Requirements
- Function `update_patient_age(db, patient_id, new_age)`
- Check if `patient_id` exists in `db`.
- If yes, update the `age` field of that patient's record and return `True`.
- If no, return `False`.

### Example
```python
# Patient 101 exists with age 30
update_patient_age(db, 101, 31)
# Patient 101 age is now 31, returns True
```

---
