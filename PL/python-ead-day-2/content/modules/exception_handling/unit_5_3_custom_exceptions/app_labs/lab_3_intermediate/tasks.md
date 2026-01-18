# Lab 3 Tasks

## Task 1: Define the Hierarchy
- Define `ClinicError(Exception)`.
- Define `SchedulingError(ClinicError)`.
- Define `BillingError(ClinicError)`.

## Task 2: Implement Operations
- Implement `book_appointment(patient, time)`. If the time is `"night"`, raise `SchedulingError("Doctors not available at night")`.
- Implement `collect_payment(amount)`. If `amount < 0`, raise `BillingError("Invalid payment amount")`.

## Task 3: Centralized Handler
- Implement `run_clinic_op(op_func, *args)`.
- Try calling `op_func(*args)`.
- Catch `ClinicError` (the base class).
- Return the error message.
- If no error, return the result of the function.
