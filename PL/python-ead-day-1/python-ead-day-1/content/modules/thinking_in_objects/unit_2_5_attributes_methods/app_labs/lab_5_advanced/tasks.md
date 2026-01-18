# Lab 5 Tasks

## Task 1: Define the Blueprint
Create a class `Ventilator`.
- Define a class attribute `service_threshold = 1000`.
- In `__init__(self, serial_no)`, initialize `self.serial_no` and `self.hours_run = 0`.

## Task 2: Implement Usage Logic
- Define `log_usage(self, hours)`: Increment the instance's `hours_run`.
- Define `check_status(self)`: Return `True` if hours meet or exceed the class threshold.

## Task 3: Simulating the Policy Shift
In `main()`:
1. Create two ventilators.
2. Log 900 hours on the first one.
3. Check status (should be `False`).
4. Update the **Class Attribute** `Ventilator.service_threshold` to 800.
5. Check status again (should now be `True`).
6. Print the results to verify that the global change affected existing objects.
