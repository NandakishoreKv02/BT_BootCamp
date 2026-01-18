# Lab 1 Tasks: Patient Lookup Optimization

## Task 1: Initialize Optimized Registry
**Difficulty**: Easy | **Points**: 20

### Objective
Prepare a high-performance registry from a legacy list.

### Requirements
- Function: `optimize_registry(legacy_list)`
- Accept a list of student/patient IDs.
- Return a `set` containing those IDs.

---

## Task 2: Fast Membership Check
**Difficulty**: Easy | **Points**: 30

### Objective
Implement a Boolean check using the optimized collection.

### Requirements
- Function: `is_id_inactive(optimized_set, target_id)`
- Use the `in` operator on the set.
- Return `True` if found, `False` otherwise.
