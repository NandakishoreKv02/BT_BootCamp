# Lab 3 Tasks: Appointment Scheduling Part 3

## Task 1: Process Waitlist
**Difficulty**: Advanced
**Points**: 20

### Objective
Move all patients from waitlist to the main schedule efficiently.

### Description
The waitlist has piled up. Move them ALL to the end of the current schedule. Clear the waitlist after moving.

### Requirements
- Function `process_waitlist(schedule, waitlist)`
- Use `list.extend()` (more efficient than loop append).
- Clear the `waitlist` list in-place (`.clear()`).
- Return the updated `schedule`.

---

## Task 2: Emergency Insert
**Difficulty**: Advanced
**Points**: 25

### Objective
Insert a high-priority appointment at the start of the day.

### Description
An emergency case needs the 09:00 slot (or just first slot). Shift everyone else down.

### Requirements
- Function `add_emergency(schedule, appointment)`
- Use `list.insert(0, appointment)`.
- Existing items shift right (indices +1).
- Return the modified schedule.

---

## Task 3: Remove Duplicates
**Difficulty**: Advanced
**Points**: 25

### Objective
Clean the list of duplicate entries preserving order.

### Description
Sometimes the receptionist double-clicks. "Smith" appears twice. Keep only the **first** occurrence.

### Requirements
- Function `remove_duplicates(schedule)`
- Return a **new list** with unique items.
- Maintain original relative order.
- Hint: Use a temporary auxiliary list (or set if we knew them, but use list check `if not in` for now).

---

## Task 4: Analytics Report
**Difficulty**: Advanced
**Points**: 30

### Objective
Generate a numbered report string list using comprehension.

### Description
Management wants a list like:
`["Slot 1: Smith", "Slot 2: Doe", ...]`

### Requirements
- Function `generate_numbered_report(schedule)`
- Use **List Comprehension** with `enumerate`.
- Return list of strings: `f"Slot {i+1}: {appt}"`.

---
