# Lab 2 Tasks: Vital Signs Monitor Part 2

## Task 1: Average Heart Rate
**Difficulty**: Intermediate
**Points**: 10

### Objective
Calculate the mean value of the heart rate field.

### Description
Given a list of tuples `(timestamp, hr, temp)`, calculate average HR.

### Requirements
- Function `calculate_average_hr(readings)`
- Loop through the list.
- Unpack the tuple to access HR (2nd element).
- Return average as float. Return 0 if list empty.

---

## Task 2: Find Fever Incidents
**Difficulty**: Intermediate
**Points**: 15

### Objective
Identify specific times when health was at risk.

### Description
Return a list of timestamps where Temperature > 38.0.

### Requirements
- Function `find_fever_incidents(readings)`
- Use tuple unpacking.
- Return list of strings (timestamps).

---

## Task 3: Generate Summary
**Difficulty**: Intermediate
**Points**: 20

### Objective
Return a summary tuple for the day.

### Description
Return a single tuple containing: `(min_hr, max_hr, avg_temp)`.

### Requirements
- Function `generate_summary(readings)`
- Find Min/Max HR and Avg Temp.
- Return the tuple.

---
