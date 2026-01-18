# Lab 1 Tasks

## Task 1: Create `Thermometer` Class
- Define class `Thermometer`.
- Implement `read(self)` returning valid temperature string (e.g., "37.5 C").

## Task 2: Create `Oximeter` Class
- Define class `Oximeter` (no inheritance from Thermometer).
- Implement `read(self)` returning valid SpO2 string (e.g., "97%").

## Task 3: Implement Reader Function
- Define `get_reading(device)`.
- It should call `device.read()` and return the result.
- Do not check the type of `device`.

## Task 4: Test
- Create a list containing one Thermometer and one Oximeter.
- Loop through the list, calling `get_reading()` on each item.
