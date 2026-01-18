# Lab 5 Tasks

## Task 1: Create the Dataset "Constructor"
Define `create_dataset(label, data_list)`:
- Returns a dictionary with keys: `'label'` and `'values'`.

## Task 2: Implement Calculation Modules
Write the following standalone math functions:
- `get_mean(values)`: Returns the average (handle empty lists).
- `get_max(values)`: Returns the largest number.
- `get_min(values)`: Returns the smallest number.

## Task 3: The Extensible Engine
Define `analyze_dataset(dataset, calc_func)`:
- This function must be "Open for Extension" but "Closed for Modification."
- It should call `calc_func` using the list from `dataset['values']`.
- Return a formatted string: `"Analysis: [LABEL] | Result: [RESULT_VALUE]"`.

## Task 4: Multi-Dimensional Research
In the `main()` function:
1. Create a dataset for "Body Temp" and another for "Blood Sugar".
2. Use the engine to find the **mean** of the temperature.
3. Use the engine to find the **max** of the blood sugar.
4. Define a NEW function `get_count` and pass it to the engine to show how easily the system extends.
