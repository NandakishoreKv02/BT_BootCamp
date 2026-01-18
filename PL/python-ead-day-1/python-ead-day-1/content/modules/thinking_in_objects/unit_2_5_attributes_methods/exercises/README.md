# Unit 2.5: Attributes and Methods - Exercises

## Overview
Now that you can build classes, it's time to master the **State** and **Behavior** within them. These exercises will challenge you to distinguish between individual object data (Instance) and shared institutional data (Class). You will also design professional method signatures and evaluate classes for the critical design principle of **Cohesion**.

## Instructions
1.  Open `unit_2_5_attributes_methods_exercises.py`.
2.  Follow the instructions in the file to implement the clinical logic.
3.  Run the file to verify your work:
    ```bash
    python unit_2_5_attributes_methods_exercises.py
    ```

## Exercise List

### 1. Unique IDs vs. Shared Clinic Name
**Concepts**: Instance Attributes, Class Attributes  
**Task**: Create a `Patient` class where every patient has their own `mrn`, but everyone shares the same `clinic_name`.

### 2. The Signature Architect
**Concepts**: Method Signatures, Arguments, Logic  
**Task**: Design a `Prescription` class with a method `update_dosage(self, new_dose, unit)`. Ensure the method signature is clear and updates the state correctly.

### 3. Global Counter
**Concepts**: Class Attribute mutation, shared state  
**Task**: Use a class attribute `total_admissions` to track how many `Patient` objects have been created across the entire application.

### 4. Cohesion Audit
**Concepts**: High Cohesion, Design Principles  
**Task**: Review a class with "mixed" responsibilities (e.g., `LabReport` that also handles `UserEmail`). Identify the non-cohesive methods that should be removed.

## Success Criteria
- All 4 tests pass the internal runner.
- Correct distinction between `self.` and `ClassName.` prefix is demonstrated.
- Methods follow the `verb_noun` naming convention.
- Class attributes are defined outside `__init__`.
