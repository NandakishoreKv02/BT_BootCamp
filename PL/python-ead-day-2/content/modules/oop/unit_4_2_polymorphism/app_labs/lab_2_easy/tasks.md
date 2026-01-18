# Lab 2 Tasks

## Task 1: Create Base `Device`
- Define `Device`.
- `start(self)` returns "Starting generic device".
- `stop(self)` returns "Stopping generic device".

## Task 2: Create `XRayMachine`
- Inherit from `Device`.
- Override `start` -> "Warming up radiation source".

## Task 3: Create `HeartMonitor`
- Inherit from `Device`.
- Override `start` -> "Calibrating sensors".

## Task 4: Polymorphic Loop
- Create a list `[XRayMachine(), HeartMonitor()]`.
- Loop through it and print the result of `start()` for each.
