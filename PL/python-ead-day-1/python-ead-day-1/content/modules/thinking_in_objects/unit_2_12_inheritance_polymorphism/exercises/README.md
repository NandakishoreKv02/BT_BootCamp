# Unit 2.12: Inheritance & Polymorphism – Exercises

## Overview
These exercises build on your knowledge of object structure to introduce hierarchy and specialized behavior. You will practice creating child classes, overriding base methods, and processing diverse objects through polymorphic loops.

## Instructions
1.  Open `unit_2_12_inheritance_exercises.py`.
2.  Complete the 4 tasks to build a functional class hierarchy.
3.  Run the file to verify your logic:
    ```bash
    python unit_2_12_inheritance_exercises.py
    ```

## Exercise List

### 1. The Staff Hierarchy
**Concepts**: Basic Inheritance  
**Task**: Create a base `Staff` class and a child `Physician` class. Ensure `Physician` inherits the `name` attribute.

### 2. Constructor Extension
**Concepts**: `super()` Keyword  
**Task**: Implement an `ElectronicDevice` class and a `SmartMonitor` child. Use `super().__init__()` to transfer the serial number while adding a `screen_size` attribute.

### 3. Specializing Behavior
**Concepts**: Method Overriding  
**Task**: Define a `DiagnosticTest` with a `perform()` method. Create a `BloodTest` subclass that overrides `perform()` to show specific hematology logic.

### 4. The Polymorphic Fleet
**Concepts**: Polymorphism  
**Task**: Create a list containing instances of `DiagnosticTest` and `BloodTest`. Iterate through them and call `.perform()` on each to see different outputs from the same call.

## Success Criteria
- Child classes correctly identify their relationship to parents.
- `super()` is used to prevent code duplication in constructors.
- Behavioral differences are evident when calling the same method name on different subtypes.
- All internal verification tests pass.
