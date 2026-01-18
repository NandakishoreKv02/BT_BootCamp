# Lab 3 Tasks

## Task 1: Parent Constructor
- Define `BasicScanner`.
- `__init__(self, model_name)`: Initialize the attribute.

## Task 2: Child Constructor with super()
- Define `MRIScanner` inheriting from `BasicScanner`.
- `__init__(self, model_name, tesla_rating)`:
  - Call `super().__init__(model_name)`.
  - Initialize `self.tesla_rating`.

## Task 3: Demonstration
In `main()`:
1. Create an `MRIScanner`.
2. Print both attributes to ensure successful inheritance.
