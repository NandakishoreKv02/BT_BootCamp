# Lab 5 Tasks

## Task 1: RecordImportError
- Define `RecordImportError(Exception)`.
- `__init__(self, message, row_idx, field)`.
- Store `row_idx` and `field`.

## Task 2: Validation
- Implement `validate_age(age_val, row_idx)`.
- If `age_val < 0`, raise `RecordImportError("Age cannot be negative", row_idx, "age")`.
- If `age_val > 150`, raise `RecordImportError("Age out of range", row_idx, "age")`.

## Task 3: Batch Process
- Implement `import_records(age_list)`.
- Iterate using `enumerate(age_list)`.
- Catch `RecordImportError`.
- For each error, append a formatted string: `f"Row {e.row_idx}: {e.field} - {e}"` to an `errors` list.
- Return `(success_count, errors)`.
