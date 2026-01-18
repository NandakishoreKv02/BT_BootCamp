# Lab 4 Tasks

## Task 1: The Base Contract
- Define `DiagnosticOutput`.
- Implement `generate_summary(self)` returning a placeholder string.

## Task 2: Subtype specializations
- Define `PhysicalExam` (Base: `DiagnosticOutput`).
  - Override `generate_summary()` with exam-specific text.
- Define `LabExam` (Base: `DiagnosticOutput`).
  - Override `generate_summary()` with lab-specific text.

## Task 3: The Polymorphic Loop
In `main()`:
1. Create a list `case_file` containing one of each instance.
2. Iterate through `case_file`.
3. Call `instance.generate_summary()` and print the result.
