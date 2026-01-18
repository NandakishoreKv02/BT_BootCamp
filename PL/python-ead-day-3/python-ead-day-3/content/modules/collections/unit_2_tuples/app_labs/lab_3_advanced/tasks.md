# Lab 3 Tasks: Vital Signs Monitor Part 3

## Task 1: Named Tuple Conversion
**Difficulty**: Advanced
**Points**: 20

### Objective
Convert raw tuples to namedtuples for better code readability.

### Description
Define a `Reading` namedtuple with fields `time`, `hr`, `temp`. Convert a list of raw tuples into a list of these objects.

### Requirements
- Function `convert_to_namedtuples(raw_data)`
- Import `namedtuple`.
- Return list of `Reading` objects.

---

## Task 2: Analyze Trends
**Difficulty**: Advanced
**Points**: 25

### Objective
Calculate the difference between the first and last reading.

### Description
Return a tuple `(hr_change, temp_change)`. Positive means increase, negative means decrease.

### Requirements
- Function `analyze_overall_trend(readings)`
- `readings` is a list of namedtuples.
- Return `(last.hr - first.hr, last.temp - first.temp)`.

---

## Task 3: Rapid Change Detection
**Difficulty**: Advanced
**Points**: 30

### Objective
Identify moments where Heart Rate jumped or dropped by > 20 bpm instantly.

### Description
Comparing consecutive readings (pairwise). If `abs(current_hr - previous_hr) > 20`, log it.

### Requirements
- Function `find_rapid_changes(readings)`
- Return a list of tuples: `(time_of_change, change_amount)`.
- Use `zip` or index loop.

---
