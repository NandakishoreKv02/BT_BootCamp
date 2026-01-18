# Lab 4 Tasks

## Task 1: Initialize
Create `make_monitor(name)`:
- Returns `{'name': name, 'hr': 70, 'status': 'Normal'}`.

## Task 2: State Transitions
Create `update_status(monitor)`:
- Increase `hr` by 25 (simulating stress).
- If `hr` < 100: status "Normal".
- If 100 <= `hr` < 140: status "Warning".
- If `hr` >= 140: status "Critical".

## Task 3: Simulation Loop
Write a loop that runs 4 times.
- In each iteration, call `update_status`.
- Print current HR and Status.
