# Lab 6 Tasks: Production System

## Task 1: Protected Collection (20 points)
Implement `CriticalCareUnit`.
- Hold patients in `_patients` (private list).
- Implement `admit_patient(patient)` and `discharge_patient(patient_id)`.
- Raise custom `CapacityError` if full.

## Task 2: Audit Logging (20 points)
Implement `_audit_log` (list).
- Every admit, discharge, or capacity change must try to append a string entry: "ACTION: Details".
- Expose a read-only property `audit_log` returning a *copy*.

## Task 3: Capacity Management (20 points)
Implement `max_capacity` property.
- Validate: must be > 0.
- If current occupancy > new max, raise `ValueError`.
- Log changes to audit log.

## Task 4: Aggregates (20 points)
Implement calculated properties:
- `occupancy_rate` (float percentage).
- `patient_ids` (list of strings, computed on fly).

## Task 5: Robustness (20 points)
Ensure:
- `admit_patient` raises `TypeError` if input isn't valid (duck typing or isinstance).
- `is_full` boolean property.
