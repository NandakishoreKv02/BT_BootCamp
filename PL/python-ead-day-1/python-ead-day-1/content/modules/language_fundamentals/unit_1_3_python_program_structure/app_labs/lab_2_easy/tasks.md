# Lab 2: Vital Signs Validator - Tasks

## Task 1: Define Constants
Define meaningful constants at the top of your file for the threshold values.
- `SPO2_CRITICAL = 90`
- `SPO2_WARNING = 95`
- `HR_CRITICAL_THRESHOLD = 120`
- `HR_WARNING_THRESHOLD = 100`

## Task 2: Implement check_vitals Function
Write the `check_vitals` function using the indentation rules strictly.

**Logic**:
- **Return "Critical"** if:
    - SpO2 is below `SPO2_CRITICAL`
    - OR (Heart Rate is above `HR_CRITICAL_THRESHOLD` AND SpO2 is below `SPO2_WARNING`)
- **Return "Warning"** if:
    - SpO2 is below `SPO2_WARNING` (but not critical)
    - OR Heart Rate is above `HR_WARNING_THRESHOLD`
- **Return "Stable"** otherwise.

**Requirements**:
- Use proper indentation.
- Use the constants you defined, not raw numbers.

## Task 3: Input Validation (Bonus)
Update the function to return "Invalid Input" if:
- SpO2 is not between 0 and 100.
- Heart Rate is negative.

## Task 4: Main Guard Test
Add a `if __name__ == "__main__":` block to run a few manual tests.
