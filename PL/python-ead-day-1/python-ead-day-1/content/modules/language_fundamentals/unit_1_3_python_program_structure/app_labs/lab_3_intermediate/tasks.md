# Lab 3: Medication Scheduler - Tasks

## Task 1: Module Structure
Organize your file with:
1. Docstring at the top.
2. Imports (`datetime`).
3. Constants (if any).
4. Functions.
5. Main execution block.

## Task 2: Implement parse_time Function
Create `parse_time(time_str)`:
- **Input**: String "HH:MM"
- **Output**: A `datetime` object (using today's date).
- **Docstring**: Required.

## Task 3: Implement calculate_next_dose Function
Create `calculate_next_dose(last_dose_time, interval_hours)`:
- **Input**: "HH:MM", integer hours.
- **Logic**: Add standard hours to the object.
- **Output**: Formatted string "HH:MM" or "HH:MM (+1 day)" if it crosses midnight.
- **Docstring**: Required.

## Task 4: Main Guard Integration
Add `if __name__ == "__main__":`:
- Ask user for input (optional) OR run hardcoded test cases.
- Should NOT run when imported.
