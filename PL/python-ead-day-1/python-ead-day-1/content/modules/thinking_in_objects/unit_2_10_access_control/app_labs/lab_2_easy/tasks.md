# Lab 2 Tasks

## Task 1: Protected State
- Define `HeartMonitor`.
- `__init__(self, bpm)`: Store `self._bpm = bpm`.

## Task 2: The Getter Property
- Add the `@property` decorator.
- Define `def bpm(self):` which returns `self._bpm`.

## Task 3: The Safety Test
In `main()`:
1. Create a `HeartMonitor(72)`.
2. Print `monitor.bpm`.
3. Wrap `monitor.bpm = 100` in a `try-except` block to catch the expected `AttributeError`.
