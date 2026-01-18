# Unit 1.4: Variables & Data Types - Exercises

## Overview
These exercises focus on Python's core data types, type system, and naming conventions.

## Instructions
1. Open `unit_1_4_variables_and_data_types_exercises.py`
2. Complete each exercise function.
3. Run the file to verify your work:
   ```bash
   python unit_1_4_variables_and_data_types_exercises.py
   ```

## Exercise List

### 1. Variable Naming (PEP 8)
Fix the provided variable names (e.g., `PatientName` -> `patient_name`) to conform to Python's standard `snake_case` convention.

### 2. Type Inspection
Use the `type()` function to return a list of types for the provided arguments.

### 3. Explicit Type Casting
Convert string inputs (e.g., "25", "1.75") into their appropriate numeric types (`int`, `float`).

### 4. String Manipulation
Create specific string formats using input data. Practice f-strings or concatenation.

### 5. Boolean Logic
Implement a simple check (`age >= 18`) that returns a Boolean (`True`/`False`).

### 6. Instance Checking
Use `isinstance()` to safely add numbers only if the inputs are valid types (`int` or `float`).

### 7. Mutability Check
Prove that integers are immutable by checking `id()` before and after modification.

### 8. Handling Type Errors
Use a `try-except` block to handle cases where type conversion might fail (like converting "abc" to int).
