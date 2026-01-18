# Lab 7 Tasks: The Ultimate Scheduler

## Task 1: Complete System Logic
**Difficulty**: Expert | **Points**: 100

### Objective
Integrate all list concepts.

### Requirements
1. **Initialize**: Create `master_schedule` (list of dicts).
2. **Add**: Function to add `{"name": str, "time": str, "dr": str}`.
3. **Sort**: Order by `time`.
4. **Filter**: Function `get_dr_queue(dr_name)` using list comprehension.
5. **Serve**: Function `serve_patient(index)` that removes from `master_schedule` and returns the patient.
6. **Summary**: Provide a list of all patient names currently in the `master_schedule`.
