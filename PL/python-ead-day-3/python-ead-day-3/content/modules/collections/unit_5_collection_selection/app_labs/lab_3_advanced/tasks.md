# Lab 3 Tasks: CCU Monitoring System

## Task 1: Real-time Status Map
**Difficulty**: Advanced | **Points**: 20

### Objective
Store patient statuses for instantaneous retrieval.

### Requirements
- Function: `update_patient_status(manager_dict, patient_id, status)`
- Add or update the patient's status in the dictionary.
- Return the dictionary.

---

## Task 2: Chronological Vitals
**Difficulty**: Advanced | **Points**: 20

### Objective
Maintain a sequential history of vitals.

### Requirements
- Function: `record_vitals(history_list, timestamp, heart_rate)`
- Append a tuple `(timestamp, heart_rate)` to the list.
- Return the list.

---

## Task 3: Unique Patient Registry
**Difficulty**: Advanced | **Points**: 20

### Objective
Track unique IDs across the day.

### Requirements
- Function: `register_visit(registry_set, patient_id)`
- Add the ID to the set.
- Return the set.

---

## Task 4: System Configuration Snapshot
**Difficulty**: Advanced | **Points**: 20

### Objective
Lock down active device IDs for auditing.

### Requirements
- Function: `lock_config(device_ids_list)`
- Convert the list of IDs into an immutable `frozenset`.
- Return the frozenset.

---

## Task 5: High-Performance Lookup Analysis
**Difficulty**: Advanced | **Points**: 20

### Objective
Verify that status lookups are efficient.

### Requirements
- Function: `batch_status_check(manager_dict, target_ids)`
- Given a list of target IDs, return a new list of their current statuses.
- Requirement: Access each status directly (O(1)) from the dictionary.
