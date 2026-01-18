# Lab 4: The Clean Documentation Cure - Tasks

## Task 1: Semantic Parameters
In `calculate_concentration`, rename:
- `d` to `dose_mg`
- `t` to `time_hr`
- `h` to `half_life`

## Task 2: PEP 8 Spacing
Ensure all math operators have spaces around them.
- `d*(0.5**(t/h))` -> `dose_mg * (0.5 ** (time_hr / half_life))`

## Task 3: Professional Docstrings
Add a Docstring following this structure:
```python
"""
Calculates the remaining drug concentration.

Args:
    dose_mg (float): Initial dose.
    time_hr (float): Time Elapsed.
    half_life (float): Drug half-life.

Returns:
    float: Remaining concentration.
"""
```

## Task 4: Code Header
Add a module-level docstring at the very top of the file explaining the purpose of the script.
