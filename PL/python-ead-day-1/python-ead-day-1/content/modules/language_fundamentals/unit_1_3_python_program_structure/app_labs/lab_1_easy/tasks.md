# Lab 1: Patient Record Formatter - Tasks

## Task 1: Create format_patient_id Function
Create a function that formats a patient ID with leading zeros.

**Requirements**:
- Function name: `format_patient_id`
- Parameter: `patient_id` (int)
- Returns: Formatted string "PAT-XXXXX" (5 digits with leading zeros)
- Must have a proper docstring with Args and Returns sections

**Example**:
```python
format_patient_id(42)  # Returns: "PAT-00042"
format_patient_id(12345)  # Returns: "PAT-12345"
```

## Task 2: Create format_patient_record Function
Create a function that formats a complete patient record.

**Requirements**:
- Function name: `format_patient_record`
- Parameters: `name` (str), `patient_id` (int), `age` (int)
- Returns: Formatted string "Patient: {name} ({formatted_id}), Age: {age}"
- Must use `format_patient_id` function
- Must have a comprehensive docstring

**Example**:
```python
format_patient_record("John Doe", 42, 35)
# Returns: "Patient: John Doe (PAT-00042), Age: 35"
```

## Task 3: Add Main Guard
Add a `__main__` guard that tests both functions when the script is run directly.

**Requirements**:
- Use `if __name__ == "__main__":`
- Test with at least 2 different patients
- Print the formatted records

## Task 4: Add Module Docstring
Add a module-level docstring at the top of the file.

**Requirements**:
- Brief description of the module's purpose
- Mention it's for healthcare patient data formatting

## Submission Checklist
- [ ] Both functions implemented
- [ ] All functions have docstrings
- [ ] Proper 4-space indentation
- [ ] `__main__` guard present
- [ ] Module docstring added
- [ ] All tests pass
