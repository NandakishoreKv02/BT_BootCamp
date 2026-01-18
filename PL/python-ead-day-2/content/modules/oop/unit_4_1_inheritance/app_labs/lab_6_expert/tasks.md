# Lab 6 Tasks

## Task 1: Create `Schedule` Class
- Attributes: `start_hour` (int), `end_hour` (int).
- Method: `is_available(hour)` returns `True` if `start <= hour < end`.

## Task 2: Refactor `Doctor` Class
- `Doctor` should accept a `schedule` object in `__init__`.
- Attributes: `name`, `schedule`.
- Method: `check_availability(hour)` delegates to `self.schedule.is_available(hour)`.

## Task 3: Create `Surgeon` Subclass
- Inherit from `Doctor`.
- Demonstrate that `Surgeon` inherits the composition logic automatically.

## Task 4: Integration
- Create a `Schedule` (09:00 to 17:00).
- Assign it to a `Surgeon`.
- Check availability at 10:00 (True) and 20:00 (False).
