# Lab 2 Tasks: Doctor Schedule Management

## Task 1: Register Doctor
**Difficulty**: Intermediate
**Points**: 10

### Objective
Create a dictionary entry with a nested structure for scheduling.

### Description
Add a doctor to the database. The `schedule` field must be initialized as an empty dictionary.

### Requirements
- Function `register_doctor(db, doc_id, name, specialty)`
- Add `doc_id` to `db`.
- Value structure:
  ```python
  {
      "name": name,
      "specialty": specialty,
      "schedule": {}  # Empty dict for now
  }
  ```
- Return `True` on success.

---

## Task 2: Initialize Schedule Slots
**Difficulty**: Intermediate
**Points**: 15

### Objective
Prepare a specific date in the doctor's schedule for appointments.

### Description
Before we can book patients, we need to "open" the schedule for a specific day. We will represent the day's slots as a list of 4 strings (e.g., "09:00", "10:00", "11:00", "12:00") stored in a dictionary? No, let's keep it key-based.
Let's make `schedule` a dictionary where **Key = Date String**, **Value = Dictionary of Slots**.
Slot Dictionary: **Key = Time String**, **Value = Patient ID (or None)**.

This is 3 levels deep: `db[doc_id]["schedule"][date][time]`.

For this task: Initialize a date with empty slots.

### Requirements
- Function `add_availability(db, doc_id, date)`
- Slots to add: "09:00", "10:00", "11:00", "14:00".
- Each slot should be initialized to `None` (empty).
- Structure:
  ```python
  db[doc_id]["schedule"][date] = {
      "09:00": None,
      "10:00": None,
      "11:00": None,
      "14:00": None
  }
  ```
- Handle missing `doc_id` (return False).

---

## Task 3: Book Appointment
**Difficulty**: Intermediate
**Points**: 20

### Objective
Update a deeply nested value safely.

### Description
Assign a patient to a specific slot. You must check if the slot is "None" (empty) before booking.

### Requirements
- Function `book_appointment(db, doc_id, date, time, patient_id)`
- Check if `doc_id` exists.
- Check if `date` exists in their schedule.
- Check if `time` exists on that date.
- Check if slot is currently `None` (available).
- If all true, update the slot with `patient_id` and return `True`.
- If any check fails (or slot is taken), return `False`.

### Edge Cases
- Doctor doesn't exist.
- Date hasn't been initialized.
- Slot is already full.

---

## Task 4: Find Doctors by Specialty
**Difficulty**: Intermediate
**Points**: 15

### Objective
Filter the database based on a criteria.

### Description
Find all doctors who specialize in a certain field.

### Requirements
- Function `find_doctors_by_specialty(db, specialty)`
- Iterate through the `db` of doctors.
- Return a **list of names** (strings) of doctors matching the specialty.
- Case-sensitive is fine for now (exact match).

### Example
```python
# Returns ["Dr. House", "Dr. Wilson"]
```

---

## Task 5: Workload Report
**Difficulty**: Intermediate
**Points**: 20

### Objective
Aggregate data from the nested structures.

### Description
Calculate how many patients a specific doctor is seeing across all dates in their schedule.

### Requirements
- Function `get_doctor_workload(db, doc_id)`
- Iterate through all dates in the doctor's `schedule`.
- Iterate through all times in each date.
- Count how many slots are NOT `None`.
- Return the total integer count.
- If doctor not found, return `None`.

---
