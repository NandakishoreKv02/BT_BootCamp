# Lab 6: Clinical Data Ingestion Engine - Tasks

## Task 1: Initialization
Define `generate_vitals_summary(filename)`. Initialize `total_hr = 0` and `count = 0`.

## Task 2: File Iteration
Open the file in read mode. Use a `for` loop to iterate through the lines.

## Task 3: Parsing and Casting
- Use `.strip()` and `.split('|')` on each line.
- If the line is empty or malformed, use `continue`.
- Cast the heart rate string to an `int`.

## Task 4: Accumulation
Add the heart rate to `total_hr` and increment `count`.

## Task 5: Summary Formatting
Print a table with the following column widths:
- Timestamp: 10
- Patient ID: 12
- Heart Rate: 8
Use f-strings like `{time:<10} | {pid:<12} | {hr:>8}`.

## Task 6: Average Calculation
Calculate `avg = total_hr / count`. Use `try/except ZeroDivisionError` in case the file is empty. Return the average.
