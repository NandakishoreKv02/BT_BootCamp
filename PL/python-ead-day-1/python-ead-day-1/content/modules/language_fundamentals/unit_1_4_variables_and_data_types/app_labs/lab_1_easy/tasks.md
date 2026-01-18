# Lab 1: Patient Data Parser - Tasks

## Task 1: Parse ID and Age
Convert `id_str` and `age_str` to integers.
- Note: Use `.strip()` to remove accidental whitespace first.

## Task 2: Parse Weight
Convert `weight_str` to float.

## Task 3: Parse Smoker Status
Convert `smoker_str` to Boolean.
- Logic: If string is "Yes", "yes", "True", or "true", return `True`.
- Otherwise return `False`.

## Task 4: Return Dictionary
Return a dictionary with keys: `id` (int), `age` (int), `weight` (float), `is_smoker` (bool).
