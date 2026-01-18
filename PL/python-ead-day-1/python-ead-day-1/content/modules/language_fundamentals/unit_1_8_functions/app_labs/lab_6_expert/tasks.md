# Lab 6: Clinical Risk Score Orchestrator - Tasks

## Task 1: Helper 1 (Age)
Define `_calc_age_factor(age)`. Return `age // 10`.

## Task 2: Helper 2 (Vitals)
Define `_calc_vital_factor(hr)`. Return `5` if `hr > 100`, otherwise `0`.

## Task 3: Helper 3 (Labs)
Define `_calc_lab_factor(has_diabetes)`. Return `10` if `True`, otherwise `0`.

## Task 4: The Orchestrator
Define `get_total_risk(age, hr, has_diabetes)`.
- Call all three helpers.
- Sum the results.
- Return the sum.

## Task 5: Abstraction
Ensure `get_total_risk` is the only function a user *needs* to call to get a complete score.
