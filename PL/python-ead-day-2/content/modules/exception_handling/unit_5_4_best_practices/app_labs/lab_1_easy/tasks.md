# Lab 1 Tasks

## Task 1: Identify LBYL
- View the `get_contact_info_legacy` function.
- It uses `if "phone" in data`.

## Task 2: Refactor to EAFP
- Implement `get_contact_info_pythonic(data, key)`.
- Use a `try` block to access `data[key]`.
- Use `except KeyError`: return `"Contact info not provided"`.

## Task 3: Test atomic access
- Verify that if the key is missing, the code handles it gracefully without crashing.
