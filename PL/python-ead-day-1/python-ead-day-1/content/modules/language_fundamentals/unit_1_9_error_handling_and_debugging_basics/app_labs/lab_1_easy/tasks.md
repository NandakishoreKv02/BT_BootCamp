# Lab 1: Patient Weight Input Guard - Tasks

## Task 1: Basic Conversion
Inside `parse_weight`, use `float(input_str)` to attempt conversion.

## Task 2: Exception Trap
Wrap the conversion in a `try` block. Add an `except ValueError:` block to catch cases where the text contains non-numeric characters.

## Task 3: Error Feedback
In the `except` block, print the exact message: "Invalid weight input: [input_str]" (replacing [input_str] with the variable).

## Task 4: Default Return
Ensure the function returns `0.0` in the error case and the converted float in the success case.
