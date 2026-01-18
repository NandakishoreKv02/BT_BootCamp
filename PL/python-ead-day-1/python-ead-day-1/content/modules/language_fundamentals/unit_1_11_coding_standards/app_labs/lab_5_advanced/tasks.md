# Lab 5: The SRP Specialist - Tasks

## Task 1: Data Cleaning Module
Write `clean_data(raw_list)`. Wrap `float(x)` in a `try/except` to skip strings like "ERROR".

## Task 2: Risk Analyzer Module
Write `analyze_risk(values)`. Return `"HIGH"` if any value is over `140.0`.

## Task 3: Reporting Module
Write `format_outcome(status)`. Return `SYSTEM REPORT: Status is [status]`.

## Task 4: The Orchestrator
In `process_labs(raw_list)`, call each helper in order and return the final string.
Observe how easy it is to test and modify each individual step compared to the monolithic function!
