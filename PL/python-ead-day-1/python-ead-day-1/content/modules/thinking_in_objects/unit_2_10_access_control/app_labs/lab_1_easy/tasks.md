# Lab 1 Tasks

## Task 1: Initialize the Sensitive State
- Define `PatientFile`.
- `__init__(self, name, id_num, ssn)`:
  - Store name as public.
  - Store id_num with a single underscore `_`.
  - Store ssn with a double underscore `__`.

## Task 2: Attempt Access
In `main()`:
1. Create a `PatientFile`.
2. Print the name and the protected ID.
3. Try to print the private SSN directly (`obj.__ssn`). Observe the error.

## Task 3: Secret Access (Mangling)
Print the SSN using the mangled name: `obj._PatientFile__ssn`.
