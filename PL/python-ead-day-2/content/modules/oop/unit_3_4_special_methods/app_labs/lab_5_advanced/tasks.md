# Lab 5 Tasks: Validation Engine

## Task 1: Create RangeValidator (20 points)
- Attributes: min_value, max_value, field_name
- Store configuration in __init__

## Task 2: Implement `__call__` for RangeValidator (20 points)
- Accept a value to validate
- Return True if within range
- Raise ValueError with descriptive message if invalid

## Task 3: Create PatternValidator (15 points)
- Accepts regex pattern in __init__
- __call__ validates string matches pattern

## Task 4: Create ValidatorChain (20 points)
- Holds list of validators
- __call__ runs all validators
- Stops on first failure

## Task 5: Validate Vital Signs (15 points)
- Temperature: 35-42 C
- Heart rate: 40-200 BPM
- Create validators for each

## Task 6: Error Messages (10 points)
- Include field name in errors
- Include actual value in errors
