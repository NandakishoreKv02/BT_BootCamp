# Unit 2.4: Identifying Classes - Exercises

## Overview
Programming isn't just about syntax; it's about **Design**. These exercises will train your brain to see the hidden classes inside messy business requirements. You will practice the Noun-Verb technique, classify objects using the BCE (Boundary-Control-Entity) pattern, and identify the dangerous "God Object" smell in code.

## Instructions
1.  Open `unit_2_4_identifying_classes_exercises.py`.
2.  Analyze the provided clinical scenarios.
3.  Complete the mapping and classification tasks.
4.  Run the file to verify your logic:
    ```bash
    python unit_2_4_identifying_classes_exercises.py
    ```

## Exercise List

### 1. The Noun-Verb Extractor
**Concepts**: Requirement Analysis, Class Identification  
**Task**: Analyze a requirement for a Pharmacy Prescription system. Identify which words are **Classes (Nouns)** and which are **Methods (Verbs)**.

### 2. The BCE Classifier
**Concepts**: Boundary, Control, Entity (BCE)  
**Task**: Take a list of clinical classes (e.g., `Patient`, `AdmissionUI`, `CalculatedRiskEngine`) and categorize them into the correct architectural tier.

### 3. Spotting the God Object
**Concepts**: Single Responsibility Principle, Cohesion  
**Task**: Examine a class called `HospitalApp`. Identify why it is a God Object and list which parts should be broken off into separate classes.

### 4. Attribute or Class?
**Concepts**: Refinement, Domain Modeling  
**Task**: Decide whether a concept like "Address" or "HeartRate" should be a standalone Class or just an Attribute of another object.

## Success Criteria
- All 4 analysis tests pass the runner.
- You can explain the difference between a "Control" class and an "Entity" class.
- You can identify at least 3 signs of a "God Object."
