# Lab 2 Tasks: Audit Log Processing

## Task 1: Map Unique Activities
**Difficulty**: Intermediate | **Points**: 30

### Objective
Filter the raw log to keep only the latest entry per user.

### Requirements
- Function: `get_latest_activities(raw_logs)`
- Iterate through `raw_logs` (list of tuples).
- Store them in a dictionary using `user_id` as the key.
- Note: Simply assigning `d[id] = log` will naturally overwrite old entries with newer ones as you iterate.
- Return the dictionary.

---

## Task 2: Format for Reporting
**Difficulty**: Intermediate | **Points**: 20

### Objective
Convert the map into an ordered list.

### Requirements
- Function: `format_sorted_report(activity_map)`
- Get all values from the dictionary.
- Convert them to a list.
- Sort the list based on the `user_id` (the first element of the tuple).
- Return the sorted list.
