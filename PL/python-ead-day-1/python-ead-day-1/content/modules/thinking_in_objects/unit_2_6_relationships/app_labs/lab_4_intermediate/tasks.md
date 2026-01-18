# Lab 4 Tasks

## Task 1: The Components
- Create `MedicalChart` (`chart_id`).
- Create `Doctor` (`name`).

## Task 2: Implement the Relationship Pair
Create a class `Patient`.
- `__init__(self, name, chart_id, doctor_obj)`:
  - Assign `self.name`.
  - Create a new `MedicalChart(chart_id)` and assign to `self.chart` (**Composition**).
  - Assign the passed `doctor_obj` to `self.primary_doctor` (**Aggregation**).

## Task 3: The Lifecycle Demo
In `main()`:
1. Create one `Doctor` instance ("Dr. Strange").
2. Create two `Patient` instances, both assigned to Dr. Strange.
3. Print the ID of each patient's chart to show they are different objects.
4. Print the name of the primary doctor for both to show they are the **same** object.
