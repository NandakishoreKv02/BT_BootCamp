# Lab 4 Tasks

## Task 1: Define Parent Classes
- Define `Doctor` with `work(self)` returning `"Treating patient"`.
- Define `Administrator` with `work(self)` returning `"Doing paperwork"`.

## Task 2: Create Child Class
- Create `ChiefMedicalOfficer` inheriting from `(Doctor, Administrator)`.
- Do NOT override `work` yet.
- Verify that calling `work()` calls the `Doctor` version (first parent).

## Task 3: Override Work
- Override `work()` in `ChiefMedicalOfficer`.
- Return a string combining both: `"Treating patient AND Doing paperwork"`.
- Use explicit calls like `Doctor.work(self)` or `super()` carefully.

## Task 4: Inspect MRO
- Print `ChiefMedicalOfficer.mro()`.
- Ensure you understand the order.
