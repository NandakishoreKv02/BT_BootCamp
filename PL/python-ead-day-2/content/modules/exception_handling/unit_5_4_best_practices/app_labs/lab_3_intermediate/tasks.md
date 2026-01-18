# Lab 3 Tasks

## Task 1: Setup
- View the `HospitalLogger` mock class.

## Task 2: Implement Logging
- Implement `safe_api_call(api_func, logger)`.
- Try calling `api_func()`.
- Catches `ConnectionError`.

## Task 3: The Right Call
- In the `except` block, call `logger.log_exception("Connection to API failed")`.
- Verify that this method is called, which in a real app would store the full traceback.
