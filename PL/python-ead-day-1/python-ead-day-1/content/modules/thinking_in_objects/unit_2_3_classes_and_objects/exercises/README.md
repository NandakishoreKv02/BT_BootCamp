# Unit 2.3: Classes and Objects - Exercises

## Overview
It's time to stop using dictionaries to "fake" objects. In these exercises, you will use the formal Python `class` keyword to create blueprints for healthcare entities. You will practice creating multiple objects from a single class and prove that while they share a blueprint, they maintain independent identities and states.

## Instructions
1.  Open `unit_2_3_classes_and_objects_exercises.py`.
2.  Complete the implementation for each exercise.
3.  Run the file to verify your work:
    ```bash
    python unit_2_3_classes_and_objects_exercises.py
    ```

## Exercise List

### 1. The Doctor Blueprint
**Concepts**: `class`, `__init__`, Attributes  
**Task**: Define a `Doctor` class that captures a doctor's name and specialty. Create two distinct doctor objects.

### 2. State vs. Identity
**Concepts**: `id()`, Object differentiation  
**Task**: Use the `id()` function to prove that two doctors with the same name are actually two different objects in memory.

### 3. Adding Behavior
**Concepts**: Methods, Behavior, `self`  
**Task**: Add an `announce()` method to your class so doctors can introduce themselves.

### 4. Updating State
**Concepts**: Attribute mutation, State change  
**Task**: Create a `Patient` class with a `status`. Write a method that changes the status from "Stable" to "Discharged".

## Success Criteria
- All 4 tests in the test runner pass.
- Class names use PascalCase.
- No global variables are used (state is stored inside `self`).
- You can explain the difference between the code you write (the class) and the data that runs (the object).
