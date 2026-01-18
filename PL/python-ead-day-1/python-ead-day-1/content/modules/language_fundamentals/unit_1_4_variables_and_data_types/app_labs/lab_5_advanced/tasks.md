# Lab 5: HL7 Field Extractor - Tasks

## Task 1: Validation
Check if string starts with "PID|". If not, raise `ValueError`.

## Task 2: Extract Fields
Using `.split('|')`:
- PID segment fields are 0-indexed in Python list.
- Field 0: "PID"
- Field 5: Name (e.g., "DOE^JOHN")
- Field 7: DOB (e.g., "19800101")
- Return dict.

## Task 3: Masking (Immutability)
Create `mask_patient_name(segment)`:
- Find the name field.
- Return a **new** string where the name is replaced by `***`.
- Verify the original string is unchanged.
