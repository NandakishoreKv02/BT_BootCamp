# Lab 5 Tasks

## Task 1: Private Helper Methods
- Implement `_fetch_raw_data()` to return a hardcoded list: `[110, 125, -5, 120, 115]`.
- Implement `_validate(data)` to filter out any values < 0.
- Implement `_compute_mean(data)` to return the average.

## Task 2: Public API
- Implement `get_average_glucose()`:
  - Call `_fetch_raw_data()`.
  - Call `_validate()` on the raw data.
  - Call `_compute_mean()` on the validated data.
  - Return the result.

## Task 3: Demo
In `main()`:
1. Create a `LabAnalytics` instance.
2. Call the public method.
3. Print the result with proper formatting.
