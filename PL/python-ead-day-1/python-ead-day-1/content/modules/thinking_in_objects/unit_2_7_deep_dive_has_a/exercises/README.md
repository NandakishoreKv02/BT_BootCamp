# Unit 2.7: Has-a Relationships – Deep Dive - Exercises

## Overview
In these exercises, you will go beyond simple object containment. You'll implement **One-to-Many** and **Many-to-Many** relationships, manage lifecycle ownership through **Composition**, and handle bidirectional links in a clinical context.

## Instructions
1.  Open `unit_2_7_deep_dive_exercises.py`.
2.  Implement the four complex relationship challenges.
3.  Run the file to verify your work:
    ```bash
    python unit_2_7_deep_dive_exercises.py
    ```

## Exercise List

### 1. One-to-Many Composition
**Concepts**: Multiplicity, Lifecycle  
**Task**: Build a `HospitalWard` that initializes with a list of `Bed` objects. If the ward is created, the beds are created within it.

### 2. Many-to-Many Aggregation
**Concepts**: Shared Associations  
**Task**: Model the relationship between `Doctor` and `Specialty`. A doctor can have multiple specialties, and a specialty belongs to many doctors.

### 3. Lifecycle Ownership (The Delete Test)
**Concepts**: Composition vs. Aggregation  
**Task**: Write code to demonstrate that a `Patient` owns their `VitalsLog` (Composition) but is only associated with their `InsuranceProvider` (Aggregation).

### 4. Bidirectional Link Sync
**Concepts**: Navigability  
**Task**: Implement a `Nurse` and a `Station`. When a nurse is assigned to a station, both objects must point to each other.

## Success Criteria
- All 4 relationship tests pass the internal runner.
- Correct use of Python lists for multiplicity.
- Logical separation between "creation during init" (Composition) and "passing into method/init" (Aggregation).
