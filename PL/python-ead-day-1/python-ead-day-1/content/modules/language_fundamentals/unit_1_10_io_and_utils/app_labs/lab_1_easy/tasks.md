# Lab 1: Interactive Triage Intake - Tasks

## Task 1: Name Collection
Define a function `run_triage()` that uses `input("Patient Name: ")` and saves it to a variable.

## Task 2: Age Collection and Conversion
Ask for age using `input("Patient Age: ")`. Convert the result to an integer.

## Task 3: Logic
- Calculate `years_left = 65 - age`.
- If `years_left > 0`, return/print: `Patient [name] will be 65 in [years_left] years.`
- Otherwise, return/print: `Patient [name] is eligible for screening.`

## Task 4: Functional Wrap
For testing purposes, ensure the function `get_screening_status(name, age)` contains the logic and returns the string, while `run_triage()` calls it.
