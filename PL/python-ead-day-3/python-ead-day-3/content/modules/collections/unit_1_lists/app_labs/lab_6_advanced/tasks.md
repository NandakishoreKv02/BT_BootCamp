# Lab 6 Tasks: Morning vs Afternoon Slots

## Task 1: Efficient Slicing
**Difficulty**: Advanced | **Points**: 100

### Objective
Segment list data into shifts.

### Requirements
- Given a list `hourly_slots` containing 24 strings (e.g., "08:00", "09:00", ...).
- Create `morning_shift` by slicing the first 12 elements.
- Create `afternoon_shift` by slicing the elements from index 12 to the end.
- Create `express_line` by taking every 3rd element from the `hourly_slots`.
- Create `last_three` using negative slicing to get the final 3 slots of the day.
