# Unit 2.11: Constructors & Lifecycle – Exercises

## Overview
These exercises focus on the mechanics of object birth. You will transition from basic state assignment to handling optional parameters, default values, and the critical "Mutable Default" trap.

## Instructions
1.  Open `unit_2_11_constructors_exercises.py`.
2.  Complete the 4 initialization challenges.
3.  Run the file to verify your logic:
    ```bash
    python unit_2_11_constructors_exercises.py
    ```

## Exercise List

### 1. The Flexible Admission
**Concepts**: Default Parameters  
**Task**: Create a `PatientAdmission` class where the `room_type` defaults to "Standard" if not provided.

### 2. The Optional Consultant
**Concepts**: Optional Parameters  
**Task**: Implement a `Consultation` class that accepts a mandatory `physician_name` and an optional `consultant_name` (defaulting to `None`).

### 3. Avoiding the Shared List Trap
**Concepts**: Mutable Default Arguments  
**Task**: Fix a broken `PharmacyOrder` class that is currently using a list `[]` as a default parameter, causing items to leak between orders.

### 4. Controlled Timestamping
**Concepts**: Automatic Initialization  
**Task**: Implement an `IncidentReport` class that automatically sets an `is_emergency` flag to `True` if the severity is 10, regardless of what the user passes.

## Success Criteria
- Objects instantiated without optional arguments use the correct defaults.
- Multiple `PharmacyOrder` objects maintain independent item lists.
- The `is_emergency` logic works correctly in the constructor.
- All internal tests pass.
