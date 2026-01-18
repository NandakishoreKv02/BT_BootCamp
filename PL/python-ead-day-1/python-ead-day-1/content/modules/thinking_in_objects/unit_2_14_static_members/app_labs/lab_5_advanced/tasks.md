# Lab 5 Tasks

## Task 1: Class Constants
- Define `SurgicalRobot`.
- Define `MIN_VOLTAGE = 110` and `MAX_VOLTAGE = 240` inside the class body.

## Task 2: Static Validation
- Implement `@staticmethod is_safe(voltage)`.
- Use the class constants to perform the check.

## Task 3: Safe Initialization
- In `__init__`, call `SurgicalRobot.is_safe(voltage)`.
- If valid: `self.voltage = voltage`.
- If invalid: `self.voltage = 0`.

## Task 4: Integration
In `main()`:
1. Try to create a robot with 220V.
2. Try to create a robot with 300V.
3. Print the results for both.
