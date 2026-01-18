# Lab 4 Tasks

## Task 1: The Processor
- Implement `process_batch(batch_list, index, key)`.
- Try to access `batch_list[index][key]`.

## Task 2: Hierarchical Catch
- Add `except LookupError as e`.
- Return a tuple: `(None, f"Lookup Failed: {str(e)}")`.

## Task 3: Success Case
- If no error, return `(found_value, "Success")`.
