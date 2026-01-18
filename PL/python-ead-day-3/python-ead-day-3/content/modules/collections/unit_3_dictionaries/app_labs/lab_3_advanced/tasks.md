# Lab 3 Tasks: Hospital Analytics System

## Task 1: Safe Merge with Conflict Logging
**Difficulty**: Advanced
**Points**: 20

### Objective
Merge two datasets while preserving the main data and tracking conflicts.

### Description
You have a `main_db` and an `archive_db`. You want to combine them.
- If an ID exists in `main_db`, KEEP IT. Do not overwrite with `archive_db`.
- If an ID exists ONLY in `archive_db`, ADD it to `main_db`.
- If an ID exists in BOTH, add the ID to a list of `conflicts`.

### Requirements
- Function `merge_datasets(main_db, archive_db)`
- Modify `main_db` in place (or return new, but let's say modify in place for efficiency).
- Return a **list** of conflicting IDs (integers).

### Example
```python
main = {1: "A"}
archive = {1: "B", 2: "C"}
conflicts = merge_datasets(main, archive)
# main is now {1: "A", 2: "C"}
# conflicts is [1]
```

---

## Task 2: Schema Validation
**Difficulty**: Advanced
**Points**: 25

### Objective
Clean dirty data by enforcing a strict schema.

### Description
Iterate through the database. Every record MUST have the keys: `"name"`, `"age"`, `"blood_type"`.
- If any key is missing, add a flag `"status": "incomplete"` to that record.
- If all keys represent valid data (simple check: name is string, age is int), ensure `"status": "active"` (unless already set).

### Requirements
- Function `validate_records(db)`
- Modify records in-place.
- Return a tuple: `(count_valid, count_incomplete)`.

---

## Task 3: Advanced Multi-Criteria Search
**Difficulty**: Advanced
**Points**: 25

### Objective
Build a flexible search engine that filters by arbitrary criteria.

### Description
The user provides a "query dictionary" like `{"blood_type": "O+", "min_age": 60}`.
You must return all records that match ALL criteria.
Supported criteria keys:
- `"blood_type"`: Exact match
- `"min_age"`: Patient age >= value
- `"max_age"`: Patient age <= value
- `"name_contains"`: Name contains string (case-insensitive)

### Requirements
- Function `search_patients(db, criteria)`
- `criteria` is a dictionary.
- Return a **list of IDs** that match.
- Use dictionary comprehensions or efficient loops.

---

## Task 4: Demographic Aggregation
**Difficulty**: Advanced
**Points**: 30

### Objective
Pivot the data to show counts by group.

### Description
Generate a report showing the distribution of patients by Blood Type.

### Requirements
- Function `get_blood_type_distribution(db)`
- Return a dictionary where Key = Blood Type, Value = Count (int).
- **Extra Challenge**: Do not count records marked `"status": "incomplete"`.

### Example
```python
# Returns
{
    "A+": 5,
    "O-": 2
}
```

---
