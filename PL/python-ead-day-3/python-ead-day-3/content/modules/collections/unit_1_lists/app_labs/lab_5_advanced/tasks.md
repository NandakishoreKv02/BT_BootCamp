# Lab 5 Tasks: Patient Queue Audit

## Task 1: Frequency and Location
**Difficulty**: Advanced | **Points**: 100

### Objective
Audit the appointment list.

### Requirements
- Given a list `queue = ["Alice", "Bob", "Emergency", "Alice", "Charlie", "Emergency"]`.
- Find how many times "Alice" appears (store in `alice_count`).
- Find the index of the first "Emergency" (store in `emergency_index`).
- Verify if "John" is in the queue using `in` (store boolean in `is_john_present`).
- Find the index of the **second** "Emergency" using the start parameter of `.index()`.
