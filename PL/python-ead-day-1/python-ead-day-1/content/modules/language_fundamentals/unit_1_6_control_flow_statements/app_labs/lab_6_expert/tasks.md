# Lab 6: Automated Billing Generator - Tasks

## Task 1: Setup
Initialize `total_cost` to `0.0`.

## Task 2: Core Loop and Skip Logic
Iterate through `procedures`. If the `status` is exactly `"Cancelled"`, use `continue`.

## Task 3: Base and Surcharge Calculation
- Add the `cost` to `total_cost`.
- If `is_emergency` is `True`, calculate 20% of that procedure's cost and add it to `total_cost`.

## Task 4: Post-Processing Discount
After the loop is finished, check if `total_cost` is greater than `500`. 
If so, apply a 10% discount (multiply by `0.9`).

## Task 5: Precision
Return the final `total_cost` rounded to 2 decimal places.
