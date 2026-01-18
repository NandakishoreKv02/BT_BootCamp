# Lab 4 Tasks

## Task 1: Create `PrescriptionRecord`
- Fields: `patient_id` (str), `medications` (list of strings).
- **CRITICAL**: Use `field(default_factory=list)` for medications to avoid shared list bugs.

## Task 2: Implement Post-Init Validation
- Add `__post_init__(self)`.
- If `patient_id` doesn't start with "P-", raise a `ValueError`.

## Task 3: Create `ArchiveRecord`
- Use the `frozen=True` flag in the dataclass decorator.
- Fields: `archive_date` (str), `content` (str).

## Task 4: Testing Immutability
- Instantiate an `ArchiveRecord`.
- Try to change its `content` and catch the `FrozenInstanceError` (import it from `dataclasses`).
