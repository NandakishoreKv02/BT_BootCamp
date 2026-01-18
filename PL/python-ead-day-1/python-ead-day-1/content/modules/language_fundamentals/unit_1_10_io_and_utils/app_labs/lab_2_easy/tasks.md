# Lab 2: Clinical Shift Report Generator - Tasks

## Task 1: Identify Parameters
Define `generate_report_row` with 3 parameters: `patient_id`, `vitals_count`, and `status`.

## Task 2: F-String Template
Construct an f-string using the following modifiers:
- `:<10` for the ID.
- `:>5` for the count.
- `:>12` for the status.

## Task 3: Delimiters
Ensure there is a space, pipe, and space (` | `) between each field.

## Task 4: Cleanup
Strip any trailing whitespace from the final string before returning it.
