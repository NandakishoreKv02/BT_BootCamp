# Lab 3 Tasks

## Task 1: Initialize the Monitor
Create a class `BPMonitor`.
- In `__init__`, store `patient_name`.
- Initialize `systolic` and `diastolic` as 0.

## Task 2: Implement Behavior
- Define `take_reading(self, s, d)`: Assign `s` to `self.systolic` and `d` to `self.diastolic`.
- Define `analyze(self)`:
  - If `systolic >= 140` or `diastolic >= 90`, return "HYPERTENSION".
  - If `systolic < 90`, return "HYPOTENSION".
  - Else, return "NORMAL".

## Task 3: Trigger Reality
In `main()`:
1. Create a monitor for "Alice".
2. Take a reading of 150/95.
3. Print the analysis result.
4. Take a second reading of 110/70.
5. Print the new analysis results to show that the object's **State** changed.
