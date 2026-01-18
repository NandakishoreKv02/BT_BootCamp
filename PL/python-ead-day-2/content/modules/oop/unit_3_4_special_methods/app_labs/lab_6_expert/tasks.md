# Lab 6 Tasks: Complete Patient Manager

## Task 1: Complete Collection Protocol (25 points)
- Implement `__len__`, `__getitem__`, `__setitem__`
- Implement `__delitem__` to remove patients
- Raise appropriate errors (IndexError, KeyError)

## Task 2: Iterator Support (15 points)
- Implement `__iter__` to yield patients
- Patients should be yielded in name order

## Task 3: Filtering (20 points)
- Implement `__call__(criteria)`
- Return new PatientManager with filtered patients
- Allow filtering by various criteria (name, dob, etc.)

## Task 4: Representations (15 points)
- `__str__` showing summary ("Manager with X patients")
- `__repr__` detailing internal state

## Task 5: Audit Trait (15 points)
- Track all additions/removals
- Log timestamp and action
- Expose audit log property

## Task 6: Robustness (10 points)
- Validate patient objects on input
- Prevent duplicate IDs
- Handle missing keys gracefully
