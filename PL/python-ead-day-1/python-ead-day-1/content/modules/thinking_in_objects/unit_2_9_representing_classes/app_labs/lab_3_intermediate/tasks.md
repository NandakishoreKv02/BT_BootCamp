# Lab 3 Tasks

## Task 1: Basic State
- Define `Prescription`.
- Constructor: `__init__(self, drug, dosage)`. Initial status is "Pending".

## Task 2: Internal Support Method
- Implement `validate(self)`.
- Print "Validating dosage...".
- Return `True` if `self.dosage <= 100`.

## Task 3: The Orchestrator Method
- Implement `fulfill(self)`.
- Use `if self.validate():` to call your validation logic internally.
- Update `self.status` if successful.

## Task 4: External Interaction
- In `main()`, create a prescription.
- Call `rx.fulfill()`.
- Print `rx.status`.
