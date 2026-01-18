# Unit 2.8: Modelling Exercises – Real-World Scenarios

## Overview
This exercise set transitions you from following instructions to making architectural decisions. You will analyze clinical needs, identify the necessary objects, and choose the most robust relationships to implement them.

## Instructions
1.  Open `unit_2_8_modelling_exercises.py`.
2.  Read the "Requirements Brief" for each exercise.
3.  Implement the classes and relationships based on the architectural constraints provided.
4.  Run the file to verify your logic:
    ```bash
    python unit_2_8_modelling_exercises.py
    ```

## Exercise List

### 1. The Noun-Verb Extracter
**Concepts**: Entity Identification  
**Task**: Given a paragraph describing a Pharmacy workflow, identify which words should be Classes and which should be Methods.

### 2. Is-a vs. Has-a: The Clinical Choice
**Concepts**: Relationship Selection  
**Task**: Implement a design for a `Ventilator` and a `Hospital`. Decide if the relationship is Inheritance or Composition and justify it through code.

### 3. Multiplicity: The Appointment Scheduler
**Concepts**: One-to-Many, Many-to-Many  
**Task**: Model a `ClinicDay`. It has many `TimeSlots` (Composition). Each `TimeSlot` is associated with one `Doctor` and one `Patient` (Aggregation).

### 4. Refactoring the God Object
**Concepts**: Cohesion, Refinement  
**Task**: Take a single "messy" `Hospital` class that stores everything and split it into several smaller, cohesive classes (`Inventory`, `Staffing`, `PatientRegistry`).

## Success Criteria
- All 4 modeling logic tests pass the runner.
- Demonstrated ability to use lists for managed collections.
- Correct implementation of constructors to enforce lifecycle rules.
- Selection of the most logical relationship for each scenario.
