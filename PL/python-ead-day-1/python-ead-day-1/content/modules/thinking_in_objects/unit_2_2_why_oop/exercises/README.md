# Unit 2.2: Why Object-Oriented Programming? - Exercises

## Overview
These conceptual exercises focus on the **Strategic** value of Object-Oriented Programming. Before mastering the syntax of classes, you must understand the "Business Case" for OOP. We will examine how industrial healthcare systems use objects to survive complexity, manage change, and scale across thousands of users.

## Instructions
1.  Open `unit_2_2_why_oop_exercises.py`.
2.  Complete each exercise by implementing the required logic or mapping.
3.  Run the file to verify your work:
    ```bash
    python unit_2_2_why_oop_exercises.py
    ```

## Exercise List

### 1. Identifying the Pillars
**Concepts**: Modularity, Reusability, Scalability  
**Task**: Categorize real-world HealthTech development scenarios into the specific OOP pillar that solves the problem (e.g., fixing a bug once vs. adding a module without breaking others).

### 2. Selecting the Paradigm
**Concepts**: Procedural, Functional, Object-Oriented  
**Task**: Choose the most efficient programming paradigm for three distinct clinical tasks: a simple file script, a pure math calculation, and a massive EHR system.

### 3. The "Ripple Effect" Analysis
**Concepts**: Maintainability, Encapsulation, Cost of Change  
**Task**: Quantify the "Cost of Change" when a core data format (like Patient ID) is modified. Compare the points of failure in a procedural system vs. an encapsulated OO system.

### 4. High Cohesion Modeling
**Concepts**: Cohesion, Data Modeling, Domain Objects  
**Task**: Identify which specific data fields and behaviors should be grouped together inside a "Prescription" object to ensure a clean, intuitive design.

## Success Criteria
- All 4 conceptual tests pass the test runner.
- You can provide a healthcare analogy for each of the four OOP pillars.
- You can explain why a complex EHR system is objectively harder to build with procedural code.
