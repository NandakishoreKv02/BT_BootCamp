# Lab 6: Dynamic Config Loader - Tasks

## Task 1: Type Inference Logic
Create `infer_type(value_str)`:
1. **None Detection**: If "none", "null" (case insensitive) -> return `None`.
2. **Boolean Detection**: If "true"/"false" -> return `bool`.
3. **Integer Detection**: If string only contains digits (or negative sign) -> return `int`.
4. **Float Detection**: If it looks like a float (contains one `.`) -> return `float`.
5. **String**: Fallback -> return original string.

## Task 2: Process Dictionary
Create `load_config(raw_config_dict)`:
- Iterate through key-value pairs.
- Apply `infer_type` to values.
- Return new dict.

## Task 3: Professional Structure
- Add docstrings.
- Handle empty inputs gracefully.
