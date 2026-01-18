# Lab 4 Tasks

## Task 1: Initialize Protected Value
- Define `VitalsMonitor`.
- `__init__(self, temp)`: Store `self._temp = temp`.

## Task 2: The Multi-View Interface
- Implement `@property` `display_temp` that returns f"{self._temp} °C".
- Implement `@property` `is_fever` that returns `self._temp > 38.0`.

## Task 3: Reporting method
- Implement `report(self)`.
- Print the display temp and whether a fever is present.

## Task 4: Dynamic Check
In `main()`:
1. Create a monitor with 37.0.
2. Call `report()`.
3. Manually update the protected `_temp` to 39.0 (simulating a sensor change).
4. Call `report()` again to see the updated property values.
