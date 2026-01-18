# Lab 1 Tasks

## Task 1: ABC Setup
- Import `ABC` and `abstractmethod`.
- Define `MedicalDevice` inheriting from `ABC`.

## Task 2: Method Contracts
- Define `operate(self)` and decorate it with `@abstractmethod`.
- Define `get_status(self)` as a normal concrete method.

## Task 3: Enforcement Test
In `main()`:
1. Use a `try-except` block.
2. Try to instantiate `MedicalDevice()`.
3. Catch the `TypeError` and print a success message.
