# Lab 6 Tasks

## Task 1: Setup the Aggregator
Create a class `PatientMetric`.
- Define two class attributes: `all_hr_sum = 0` and `total_patients = 0`.
- In `__init__(self, name)`:
  - Store `self.name` and initialize `self.reading = 0`.
  - Increment the class `total_patients` count.

## Task 2: Implement the Linked behavior
- Define `record_heart_rate(self, bpm)`:
  - Update `self.reading`.
  - Add the reading to the class `all_hr_sum`.

## Task 3: The Aggregation Logic
- Define a method (can be regular or static/class, but use `PatientMetric.attr` for simplicity) called `get_average_bpm()`.
- Return the result of `all_hr_sum / total_patients`.
- Add a check to return 0 if `total_patients` is 0.

## Task 4: Stress Test the Aggregator
In `main()`:
1. Create "Bob" and "Alice".
2. Record 80 bpm for Bob and 100 bpm for Alice.
3. Print the clinic average (should be 90.0).
4. Create "Charlie", record 60 bpm.
5. Print the new average (should be 80.0).
