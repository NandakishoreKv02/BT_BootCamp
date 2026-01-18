# Unit 2.15: Abstraction & Design Principles – Exercises

## Overview
These exercises focus on the architectural side of Python OOP. You will practice defining strict contracts using Abstract Base Classes and refactoring code to adhere to the Single Responsibility Principle.

## Instructions
1.  Open `unit_2_15_abstraction_exercises.py`.
2.  Follow the 4 tasks to master abstraction and SRP.
3.  Run the file to verify:
    ```bash
    python unit_2_15_abstraction_exercises.py
    ```

## Exercise List

### 1. The Abstract Treatment
**Concepts**: ABC and @abstractmethod  
**Task**: Create an abstract class `Treatment` with an abstract method `administer()`. Ensure that trying to instantiate `Treatment` directly raises a `TypeError`.

### 2. Concrete Implementation
**Concepts**: Subclassing ABCs  
**Task**: Create a `Vaccine` class that inherits from `Treatment` and implements the `administer()` method.

### 3. SRP Refactoring
**Concepts**: Single Responsibility Principle  
**Task**: Take a "God Class" `PatientManager` (which handles data AND billing) and split it into two separate classes: `Patient` and `InvoiceGenerator`.

### 4. Interface Enforcement
**Concepts**: Contractual Consistency  
**Task**: Ensure that multiple subclasses (`BloodTest`, `XRay`) all implement a mandatory `get_cost()` method defined in their abstract parent.

## Success Criteria
- Abstract classes cannot be instantiated.
- Concrete subclasses provide meaningful implementations for all abstract methods.
- Responsibility is clearly separated between classes.
- All internal validation tests pass.
