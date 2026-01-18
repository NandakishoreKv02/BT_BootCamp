# Lab 3 Tasks

## Task 1: Record Creation
Create `create_triage_record(name, age, heart_rate, complaint)`:
- Returns `{'name': ..., 'age': ..., 'hr': ..., 'complaint': ..., 'priority': 'Normal'}`.

## Task 2: Logic Modules
Create `assess_severity(record)`:
- If `hr > 120` or `complaint == "Chest Pain"`, set `priority` to "HIGH".

Create `print_wristband(record)`:
- Prints formatted details.

## Task 3: Integration
Write a script that processes a patient "John Doe" (HR: 130) and "Jane Smith" (HR: 70).
Process both through the pipeline.
