# Lab 1 Tasks

## Task 1: Create `VitalsRecord` Dataclass
- Use the `@dataclass` decorator.
- Fields: `heart_rate` (int), `temperature` (float), `blood_pressure` (str).

## Task 2: Create `PatientHeader` Dataclass
- Fields: `patient_id` (str), `name` (str), `ward` (str).

## Task 3: Initialization
- Instantiate a `PatientHeader` and a `VitalsRecord`.
- Print both to verify the auto-generated `__repr__`.

## Task 4: Equality Check
- Create two identical `VitalsRecord` objects and use `==` to verify that dataclasses provide value-based equality by default.
