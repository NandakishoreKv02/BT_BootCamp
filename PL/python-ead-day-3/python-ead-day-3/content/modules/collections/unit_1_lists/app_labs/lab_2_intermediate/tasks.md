# Lab 2 Tasks: Appointment Scheduling Part 2

## Task 1: Cancel Appointment
**Difficulty**: Intermediate
**Points**: 10

### Objective
Remove an appointment from the list safely.

### Description
The receptionist needs to delete a booking.
If the appointment string exists, remove it. If it doesn't exist, do nothing (do not crash).

### Requirements
- Function `cancel_appointment(schedule, appointment_string)`
- Use `list.remove()` or check existence first.
- Return `True` if removed, `False` if not found.
- **Do not** raise a ValueError.

---

## Task 2: Organize Schedule
**Difficulty**: Intermediate
**Points**: 15

### Objective
Sort the appointments chronologically.

### Description
The lists are currently entered in random order. Since we use "HH:MM" format at the start of the string, standard alphabetical sorting works perfectly for chronological order.

### Requirements
- Function `organize_schedule(schedule)`
- Modify the list **in-place** to be sorted.
- Return the sorted list (for convenience, though it is modified in place).

### Example
```python
Input: ["14:00 - B", "09:00 - A"]
Result: ["09:00 - A", "14:00 - B"]
```

---

## Task 3: Get Morning Shift
**Difficulty**: Intermediate
**Points**: 20

### Objective
Extract appointments before 12:00.

### Description
The doctors want a list of just the morning patients.

### Requirements
- Function `get_morning_appointments(schedule)`
- Return a **new list** containing only appointments starting strictly before "12:00".
- Assume schedule is sorted (or sort it first). or just iterate and filter.
- Iterate and filter is safer if not sorted.

---

## Task 4: Find Patient Slot
**Difficulty**: Intermediate
**Points**: 15

### Objective
Search for a patient's time slot by name.

### Description
A patient calls asking "When is my appointment?". You have their name (e.g., "Smith"). You need to find the string containing "Smith" and return it.

### Requirements
- Function `find_patient_slot(schedule, patient_name)`
- Search for the string that **contains** `patient_name`.
- Return the full appointment string (e.g., "14:00 - John Smith").
- If multiple match, return the first one.
- If none, return `None`.

---
