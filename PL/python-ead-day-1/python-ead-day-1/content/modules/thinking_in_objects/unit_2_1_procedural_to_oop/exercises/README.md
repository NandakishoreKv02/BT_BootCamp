# Unit 2.1: From Procedural to Object-Oriented Thinking - Exercises

## Overview
These exercises bridge the gap between procedural "scripting" and architectural "object-oriented" design. We will focus on **refactoring**, **state management**, and **domain modeling** within a Healthcare context. 

We will not use the `class` keyword yet. Instead, we will simulate objects using dictionaries (Proto-Objects) to understand *why* classes are necessary.

## Instructions
1.  Open `unit_2_1_procedural_to_oop_exercises.py`.
2.  Complete each exercise by implementing the required functionality.
3.  Run the file to verify your work:
    ```bash
    python unit_2_1_procedural_to_oop_exercises.py
    ```

## Exercise List

### 1. The Global Patient List Trap
**Concepts**: Scope, Global Variables, Refactoring  
**Task**: Fix a broken function that tries to update a global "admitted patient" status without permission. Understand why global state is dangerous in clinical systems.

### 2. Grouping Data (The Proto-Object)
**Concepts**: Data Structures, Dictionaries, Refactoring  
**Task**: Convert three separate "parallel lists" (MRNs, Names, Priorities) into a single list of structured Patient dictionaries. This creates high Cohesion.

### 3. Encapsulation (Updating Vitals)
**Concepts**: State Management, Mutable Data  
**Task**: Write a function that takes a Patient "Object" (dictionary) and updates its vital signs "state" safely, effectively simulating a method.

### 4. Hospital System Analysis
**Concepts**: OOP Design, Requirement Analysis  
**Task**: Analyze a written requirement about prescriptions and pharmacists to identify the key "Nouns" that should become software Objects.

### 5. BMI vs Patient Chart (Stateless vs Stateful)
**Concepts**: State, Pure Functions vs Objects  
**Task**: Distinguish between concepts that need Memory (Stateful Objects like Charts) and those that are just Calculations (Stateless Functions like BMI).

### 6. Digital Prescriptions (Constructor Pattern)
**Concepts**: Factory Functions, Initialization, State Change  
**Task**: Create a "Factory" function that produces standardized Prescription dictionaries, and another function to modify their status (e.g., Discontinue).

## Success Criteria
- All 6 tests pass without error.
- "Global" keyword is used correctly (Exercise 1 only).
- Data is consistently structured in dictionaries.
- You can explain *why* `patient = {'name': 'Alice'}` is better than `patient_name = 'Alice'`.
