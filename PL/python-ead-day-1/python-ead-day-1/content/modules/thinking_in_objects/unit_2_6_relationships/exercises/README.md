# Unit 2.6: Relationships Between Classes - Exercises

## Overview
Objects in a complex system like a hospital are like pieces of a puzzle—they only make sense when they are connected. These exercises will train your brain to identify and implement the three core relationships: **Inheritance** (Is-a), **Composition** (Has-a), and **Dependency** (Uses).

## Instructions
1.  Open `unit_2_6_relationships_exercises.py`.
2.  Analyze the clinical scenarios provided.
3.  Complete the mapping, implementation, and refinement tasks.
4.  Run the file to verify your logic:
    ```bash
    python unit_2_6_relationships_exercises.py
    ```

## Exercise List

### 1. The Relationship Classifier
**Concepts**: Identification, Modeling  
**Task**: Take a list of clinical class pairs (e.g., `Nurse/Person`, `Hospital/Ward`, `Surgeon/Scalpel`) and determine if the relationship is Inheritance, Composition, or Dependency.

### 2. Composition vs. Aggregation
**Concepts**: Has-a (Strong vs. Weak)  
**Task**: Implement a `Patient` that "owns" its `MedicalRecord` (Composition) but is simply "associated" with a `PrimaryDoctor` (Aggregation).

### 3. The Dependency Injector
**Concepts**: Uses (Dependency)  
**Task**: Implement a `ReportGenerator` class that doesn't own any data, but "uses" a `Patient` object passed to its method to produce a summary.

### 4. Spotting Modeling Mistakes
**Concepts**: Inheritance Abuse  
**Task**: Identify why making `Patient` inherit from `BloodPressureMonitor` is a mistake and explain what the relationship should actually be.

## Success Criteria
- All 4 modeling tests pass the internal runner.
- You can explain why Composition is generally favored over Inheritance.
- Correct implementation of "Has-a" using constructor assignment.
- Correct implementation of "Uses" using method arguments.
