# Lab 3 Tasks

## Task 1: Create the Validator "Constructor"
Define `make_validator()`:
- Returns a dictionary with an empty list under the key `'rules'`.

## Task 2: Rule Management
Define `add_rule(validator, rule_function)`:
- Accept the validator object and a function reference as arguments.
- Append the function reference to the `rules` list.

## Task 3: The Validation Engine
Define `run_validation(validator, patient_dict)`:
- Create an empty `errors` list.
- Loop through all functions stored in `validator['rules']`.
- Call each function with `patient_dict`.
- If a function returns an error string, add it to the `errors` list.
- Return the list of all errors.

## Task 4: Implement Clinical Rules
Create standalone functions:
- `check_mrn(patient)`: Returns "MRN must be 6 digits" if invalid.
- `check_age(patient)`: Returns "Age cannot be negative" if invalid.
- `check_name(patient)`: Returns "Name cannot be empty" if invalid.

## Task 5: Main Simulation
1. Initialize a validator.
2. Plug in all three rules.
3. Test with a patient record that has multiple errors.
4. Verify that the engine caught all errors without needing separate "if" statements for each rule.
