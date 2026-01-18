# Lab 4 Tasks: Diagnosis Codes

## Task 1: Create DiagnosisCode (15 points)
- Attributes: code (str), description (str)

## Task 2: Implement `__eq__` (25 points)
- Compare by code only
- Return NotImplemented for non-DiagnosisCode

## Task 3: Implement `__hash__` (25 points)
- Hash based on code
- Equal objects must have equal hashes

## Task 4: Test Set Usage (20 points)
- Add same code twice to a set
- Verify only one instance remains

## Task 5: Test Dict Usage (15 points)
- Use DiagnosisCode as dictionary key
- Verify lookup works correctly
