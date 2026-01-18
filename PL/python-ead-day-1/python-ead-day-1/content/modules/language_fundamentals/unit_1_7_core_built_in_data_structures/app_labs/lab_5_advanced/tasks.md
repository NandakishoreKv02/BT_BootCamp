# Lab 5: Lab Result Batch Processor - Tasks

## Task 1: Filtering
Create an empty list named `filtered_results`. Iterate through the `batch`. If the `type` matches the `test_type` parameter, add the dictionary to `filtered_results`.

## Task 2: Transformation
Loop through `filtered_results`:
- Access the `"val"`.
- If `"val"` is greater than `threshold`, set a new key `"is_alert"` to `True` in that dictionary.
- Otherwise, set `"is_alert"` to `False`.

## Task 3: Aggregation
Calculate the average of the `"val"` fields from the `filtered_results`. 
Average = Sum / Count. (Handle the case where count is 0 by returning 0.0).

## Task 4: Return
Return a tuple containing the `(average, filtered_results)`.
