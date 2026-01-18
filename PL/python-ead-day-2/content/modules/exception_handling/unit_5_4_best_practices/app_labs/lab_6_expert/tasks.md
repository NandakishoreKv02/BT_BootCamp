# Lab 6 Tasks

## Task 1: The EAFP Filter
- Implement `filter_stream_eafp(streaming_data)`.
- Use a `try` block for each item.
- Operation: `float(item)`.
- Catch `(ValueError, TypeError)` and skip if they occur.
- Return the sum of all valid floats.

## Task 2: The LBYL Filter
- Implement `filter_stream_lbyl(streaming_data)`.
- Use an `if` check for each item.
- Check if `isinstance(item, (int, float))` OR if it's a digit string.
- Return the sum.

## Task 3: Optimization Analysis
- In your own mind, consider: If 99% of data is valid, which is faster? (Answer: EAFP). If 50% is bad? (Answer: LBYL).
