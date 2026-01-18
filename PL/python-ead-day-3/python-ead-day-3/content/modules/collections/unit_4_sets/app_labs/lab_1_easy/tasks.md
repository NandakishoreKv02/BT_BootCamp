# Lab 1 Tasks: Hospital Registry

## Task 1: Initialize Registry
**Difficulty**: Easy | **Points**: 10

### Objective
Convert a list of patient visit logs into a unique set.

### Requirements
- Function: `initialize_registry(visiting_ids)`
- Accept a list of integers (IDs).
- Return a `set` containing those IDs.

---

## Task 2: Robust Check-in
**Difficulty**: Easy | **Points**: 15

### Objective
Add a patient to the registry.

### Requirements
- Function: `check_in_patient(registry, patient_id)`
- Add the `patient_id` to the existing `registry` set.
- Return the updated set.

---

## Task 3: Safe Removal
**Difficulty**: Easy | **Points**: 15

### Objective
Remove a patient from the registry without crashing if they aren't there.

### Requirements
- Function: `remove_record(registry, patient_id)`
- Use a safe set method (e.g., `.discard()`) to remove the ID.
- Return the updated set.

---

## Task 4: Get Statistics
**Difficulty**: Easy | **Points**: 10

### Objective
Return the total count of unique patients.

### Requirements
- Function: `get_unique_count(registry)`
- Return the length of the set.
