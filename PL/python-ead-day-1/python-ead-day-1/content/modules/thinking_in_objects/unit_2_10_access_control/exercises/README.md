# Unit 2.10: Access Control & Encapsulation – Exercises

## Overview
These exercises focus on protecting data integrity. You will practice using underscores to signal visibility and the `@property` decorator to implement logic-gate getters and setters for medical data.

## Instructions
1.  Open `unit_2_10_access_control.py`.
2.  Follow the requirements for each exercise to implement access control.
3.  Run the file to verify your logic:
    ```bash
    python unit_2_10_access_control.py
    ```

## Exercise List

### 1. Naming Signals
**Concepts**: `_` vs `__`  
**Task**: Take a `Patient` class and modify its attributes: make `name` public, `_internal_id` protected, and `__ssn` private.

### 2. The Read-Only Property
**Concepts**: `@property` (Getter)  
**Task**: Implement a `HeartRate` class where the `bpm` value can only be read, never changed after initialization.

### 3. The Validating Setter
**Concepts**: `@attr.setter`  
**Task**: Create a `BloodSugar` class. Use a setter to ensure the `level` cannot be set to a value below 0 or above 1000.

### 4. Handling Mangled Names
**Concepts**: Name Mangling  
**Task**: Access a private attribute (`__secret`) from outside the class using the mangled name syntax (`_ClassName__secret`) to demonstrate your understanding of how Python stores it.

## Success Criteria
- Direct assignment to `__ssn` fails or is ignored.
- The `HeartRate` class raises an `AttributeError` if a user tries to set the bpm.
- The `BloodSugar` setter successfully blocks invalid (e.g., negative) inputs.
- All tests in the file pass correctly.
