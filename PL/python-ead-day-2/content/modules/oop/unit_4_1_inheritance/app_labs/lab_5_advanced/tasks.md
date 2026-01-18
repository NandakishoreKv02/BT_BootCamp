# Lab 5 Tasks

## Task 1: Define ABC `MedicalProcedure`
- Import `ABC` and `abstractmethod` from `abc`.
- Define `MedicalProcedure` inheriting from `ABC`.
- Define abstract methods `perform(self)` and `get_duration(self)`.

## Task 2: Implement `Surgery`
- Inherit from `MedicalProcedure`.
- Implement `perform` returning `"Performing surgery"`.
- Implement `get_duration` returning `60`.

## Task 3: Implement `Checkup`
- Inherit from `MedicalProcedure`.
- Implement `perform` returning `"Performing checkup"`.
- Implement `get_duration` returning `15`.

## Task 4: Incomplete Implementation
- Create a class `XRay` that inherits from `MedicalProcedure` but only implements `perform`.
- Try to instantiate it in a test/script and observe the `TypeError`.
