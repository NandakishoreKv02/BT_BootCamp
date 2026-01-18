# Unit 2.16: Putting It All Together – Exercises

## Overview
These exercises are designed to test your ability to convert messy, procedural logic into clean, object-oriented systems. You will refactor code, design classes from scratch, and fix architectural anti-patterns.

## Instructions
1.  Open `unit_2_16_capstone_exercises.py`.
2.  Follow the tasks to refactor and implement the clinical systems.
3.  Run the file to verify:
    ```bash
    python unit_2_16_capstone_exercises.py
    ```

## Exercise List

### 1. Refactoring "The Script"
**Concepts**: Functions to Classes  
**Task**: Convert a script that uses global dictionaries to track `Inventory` into a proper `InventoryManager` class with methods like `add_item` and `dispense`.

### 2. The God Object Fix
**Concepts**: SRP and Decomposition  
**Task**: A `HospitalSuperSystem` class handles admissions AND cafeteria food. Split it into `AdmissionOffice` and `Cafeteria`.

### 3. The Data Clump
**Concepts**: Encapsulation  
**Task**: A method `create_appointment(d_name, d_spec, d_room, p_name)` takes too many arguments. Refactor it to accept `Doctor` and `Patient` objects.

### 4. Full Flow Integration
**Concepts**: Interaction  
**Task**: Create a `BloodBank` and `Donor` system. Ensure `BloodBank` can check eligibility based on `Donor` attributes and update its stock.

## Success Criteria
- Global state is eliminated in favor of instance state.
- Classes have single, clear responsibilities.
- Methods accept Objects rather than long lists of primitives.
- The system functions end-to-end without errors.
