# Lab 4 Tasks: Immutability and Nested Data

## Task 1: Explore Tuple Integrity
**Difficulty**: Advanced | **Points**: 100

### Objective
Understand pointer-level immutability.

### Requirements
- Create a tuple `study_data` containing: `"Project-X"`, `[10, 20, 30]`.
- Attempt to reassign `study_data[1] = [40, 50]` and wrap it in a `try-except` to catch the `TypeError`.
- Successfully append `40` to the list at `study_data[1]`.
- Prove that the tuple's *structure* is fixed but its *content* (if mutable) is not.
