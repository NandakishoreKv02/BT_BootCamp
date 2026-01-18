# Lab 3: Insurance Coverage Lookup - Tasks

## Task 1: Primary Lookup
Inside `fetch_provider_id`, use `try` to access the `"provider_id"` key.

## Task 2: Handle Missing Info
Catch `KeyError`.

## Task 3: Secondary Action (Logging)
Inside the `except KeyError:` block:
- Extract the `"name"` from the dictionary.
- Print exactly: `LOG: Missing provider ID for patient [name]`.

## Task 4: Fallback Return
Return the string `"PENDING_VERIFICATION"` inside the except block.
