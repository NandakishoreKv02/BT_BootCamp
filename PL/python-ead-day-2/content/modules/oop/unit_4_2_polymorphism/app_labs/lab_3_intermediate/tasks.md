# Lab 3 Tasks

## Task 1: Create `VitalSign` Class
- `__init__(self, value, unit)`.
- `__str__(self)` returns "value unit" (e.g., "120 mmHg").

## Task 2: Implement Comparison
- Implement `__gt__(self, other)`.
- Implement `__lt__(self, other)`.
- Both checks:
  1. If `other` is not `VitalSign`, raise `TypeError`.
  2. If `self.unit != other.unit`, raise `ValueError`.
  3. Otherwise, compare `self.value` and `other.value`.

## Task 3: Test Comparisons
- Check if `VitalSign(99, "F") > VitalSign(98.6, "F")` is True.
- Check if `VitalSign(99, "F") > VitalSign(37, "C")` raises ValueError.

## Task 4: `check_alert` Function
- Takes `current_reading` and `threshold`.
- Returns "CRITICAL" if current > threshold, else "NORMAL".
