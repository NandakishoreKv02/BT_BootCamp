# Unit 1.9: Error Handling & Debugging Basics - Exercises

## Overview
These exercises focus on making your clinical applications robust against unexpected data and runtime errors. You will practice using `try/except` blocks to handle common healthcare data pitfalls.

## Instructions
1. Open `unit_1_9_error_handling_exercises.py`.
2. Complete each exercise function using specific exception handling.
3. Run the file to verify your work:
   ```bash
   python unit_1_9_error_handling_exercises.py
   ```

## Exercise List

### 1. Dosage Guard (ZeroDivisionError)
Handle the scenario where a user enters "0" for the number of doses in a day.

### 2. Vital Parser (ValueError)
Safely convert string-based sensor data to numbers, handling invalid text like "N/A".

### 3. Record Guard (KeyError)
Safely access patient demographics in a dictionary where some keys might be missing.

### 4. Reading Guard (IndexError)
Safely access the most recent vital sign in a measurement list that might be empty.

### 5. Multi-Trap (Complex Handling)
Handle data retrieval, conversion, and division in a single block with three specific `except` handlers.

### 6. Cleanup (Finally Block)
Ensure that an "Operation Logged" message is returned regardless of whether an addition operation succeeds or fails.
