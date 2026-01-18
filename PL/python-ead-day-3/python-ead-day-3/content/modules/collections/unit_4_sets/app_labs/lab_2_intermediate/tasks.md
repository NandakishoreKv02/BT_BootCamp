# Lab 2 Tasks: Patient Flow Analysis

## Task 1: Find Overlapping Patients
**Difficulty**: Intermediate | **Points**: 15

### Objective
Identify patients who visited both the ER and the ICU.

### Requirements
- Function: `get_shared_patients(er_set, icu_set)`
- Use the intersection operator (`&`).
- Return a set of IDs found in both.

---

## Task 2: Combine All Patients
**Difficulty**: Intermediate | **Points**: 15

### Objective
Get a single set of all unique patients who visited either department.

### Requirements
- Function: `get_all_unique_patients(er_set, icu_set)`
- Use the union operator (`|`).
- Return a single combined set.

---

## Task 3: Identify Non-Admitted ER Patients
**Difficulty**: Intermediate | **Points**: 20

### Objective
Find patients who were in the ER but were NOT admitted to the ICU.

### Requirements
- Function: `get_er_only_patients(er_set, icu_set)`
- Use the difference operator (`-`).
- Note: Order matters for the difference operation.

---

## Task 4: Find Single-Department Visitors
**Difficulty**: Intermediate | **Points**: 20

### Objective
Find patients who visited ONLY one of the departments (either ER or ICU, but not both).

### Requirements
- Function: `get_single_dept_visitors(er_set, icu_set)`
- Use the symmetric difference operator (`^`).
- Return a set of IDs unique to one department.
