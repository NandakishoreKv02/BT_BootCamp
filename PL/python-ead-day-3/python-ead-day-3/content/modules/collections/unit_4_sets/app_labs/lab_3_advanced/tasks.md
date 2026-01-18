# Lab 3 Tasks: Staffing Audit

## Task 1: Compliance Check (Subsets)
**Difficulty**: Advanced | **Points**: 15

### Objective
Determine if all staff working a shift are authorized.

### Requirements
- Function: `is_shift_compliant(ward_staff, master_authorized)`
- Return `True` if `ward_staff` is a subset of `master_authorized`, `False` otherwise.
- Use the `.issubset()` method.

---

## Task 2: Double-Shift Detection (Disjoint Sets)
**Difficulty**: Advanced | **Points**: 15

### Objective
Ensure that no staff members are working both the Morning and Night shifts simultaneously.

### Requirements
- Function: `no_double_shift_violations(morning_shift, night_shift)`
- Return `True` if the two sets share NO elements.
- Use the `.isdisjoint()` method.

---

## Task 3: Immutable Certification Set
**Difficulty**: Advanced | **Points**: 15

### Objective
Create a fixed, immutable set of required certifications.

### Requirements
- Function: `create_fixed_requirements(cert_list)`
- Convert the input list into a `frozenset`.
- Return the `frozenset`.

---

## Task 4: Filter Senior Staff (Set Comprehension)
**Difficulty**: Advanced | **Points**: 20

### Objective
Extract a unique set of "Senior" staff (IDs greater than 5000) from a list of shift logs.

### Requirements
- Function: `get_senior_staff(shift_data)`
- Use a **set comprehension**.
- Filter for items `> 5000`.
- Return the resulting set.

---

## Task 5: Find Unauthorized Personnel
**Difficulty**: Advanced | **Points**: 20

### Objective
Specifically identify the IDs of people working who are NOT authorized.

### Requirements
- Function: `identify_unauthorized_ids(ward_staff, master_authorized)`
- Use set difference to find IDs in `ward_staff` but not in `master_authorized`.
- Return a set of offending IDs.
