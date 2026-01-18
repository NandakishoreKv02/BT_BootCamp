# Unit 2.13: Method Overloading & Python's Approach – Exercises

## Overview
These exercises teach you how to create flexible method interfaces using Pythonic strategies. You will move away from fixed signatures to methods that adapt based on the data provided.

## Instructions
1.  Open `unit_2_13_overloading_exercises.py`.
2.  Follow the tasks to implement flexible medical logic.
3.  Run the file to verify:
    ```bash
    python unit_2_13_overloading_exercises.py
    ```

## Exercise List

### 1. The Adaptive Dosage
**Concepts**: Default Arguments  
**Task**: Create a `DoseAdmin` class with a `prescribe` method. It should take a `medicine` name and an optional `dose_mg` (default 10mg).

### 2. The Vital Aggregator
**Concepts**: Variable Arguments (`*args`)  
**Task**: Implement a `HealthLog` with a `record_bp` method that can take any number of blood pressure readings at once and return their average.

### 3. The Meta-Patient Record
**Concepts**: Keyword Arguments (`**kwargs`)  
**Task**: Create a `PatientRecord` with an `update` method. It should accept any number of named attributes (e.g., `age=30`, `city="London"`) and store them in a dictionary.

### 4. Logic Branching
**Concepts**: Input Validation  
**Task**: Implement a `Finder` class with a `search` method. If the input is an `int`, search by ID; if it is a `str`, search by Name.

## Success Criteria
- Methods can be called with varying argument counts without crashing.
- `*args` correctly processes multiple inputs.
- `**kwargs` correctly captures metadata.
- All internal validation tests pass.
