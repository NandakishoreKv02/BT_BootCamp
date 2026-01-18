# Lab 6 Tasks

## Task 1: The Base Variable
- Define `Treatment`.
- `__init__(self, name)`.
- `get_intensity_score(self)`: Return 0 (placeholder).

## Task 2: Implementing Logic Overrides
- Define `DrugTherapy`.
  - `__init__(self, name, dosage_mg)`.
  - Override `get_intensity_score()` to return `dosage_mg * 2`.
- Define `ClinicalExercise`.
  - `__init__(self, name, minutes)`.
  - Override `get_intensity_score()` to return `minutes / 2`.

## Task 3: The Aggregator Class
- Define `CarePlan`.
- `__init__(self, patient_name)`.
- `add_treatment(self, treatment)`.
- `total_intensity(self)`:
  - Loop through treatments.
  - Sum the result of `item.get_intensity_score()`.

## Task 4: Complete Workflow
In `main()`:
1. Create a `CarePlan`.
2. Add one drug therapy and one exercise.
3. Print the individual scores and the total plan score.
