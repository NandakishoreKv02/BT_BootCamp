# Unit 2.14: Static Members & Utility Behavior – Exercises

## Overview
These exercises focus on functionality that belongs to the class blueprint rather than specific objects. You will practice managing shared counters, creating utility toolkits, and implementing alternative object creation paths.

## Instructions
1.  Open `unit_2_14_static_exercises.py`.
2.  Follow the 4 tasks to master class-level logic.
3.  Run the file to verify:
    ```bash
    python unit_2_14_static_exercises.py
    ```

## Exercise List

### 1. The Hospital Population
**Concepts**: Static Variables  
**Task**: Add a class variable `population` to `Patient`. Increment it every time a new instance is born.

### 2. The Dosage Toolkit
**Concepts**: Static Methods (`@staticmethod`)  
**Task**: Create a `MedMath` class with a static method `to_grams(mg)` that performs a simple division by 1000.

### 3. The Dictionary Intake
**Concepts**: Class Methods (`@classmethod`)  
**Task**: Use a class method `from_dict(cls, data)` to create a `Staff` object from a provided Python dictionary.

### 4. Instance vs Static
**Concepts**: Design Choice  
**Task**: Implement a method that correctly chooses between `@staticmethod` and a regular method for a "Health Check" verification.

## Success Criteria
- Global counters accurately reflect object counts.
- Static methods are accessible without instantiating the class.
- Factory methods return valid class instances.
- All internal validation tests pass.
