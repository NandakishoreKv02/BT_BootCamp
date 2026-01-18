# Lab 5: Multi-Level Data Deep Diver - Tasks

## Task 1: The Deep Dive
In `extract_weight`, attempt to access `data["patient"]["observations"]["weight"]` and convert it to a `float` in one line.

## Task 2: Specific Exception Handlers
Implement three separate `except` blocks.
- `except KeyError:` -> `return "DATA_MISSING"`
- `except ValueError:` -> `return "INVALID_FORMAT"`
- `except TypeError:` -> `return "TECHNICAL_ERROR"`

## Task 3: Success Path
Ensure the float value is returned if no exception occurs.
