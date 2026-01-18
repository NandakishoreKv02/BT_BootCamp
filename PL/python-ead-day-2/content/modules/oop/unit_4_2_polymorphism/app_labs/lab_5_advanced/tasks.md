# Lab 5 Tasks

## Task 1: Initialize `VitalHistory`
- Create class `VitalHistory`.
- `__init__(self, readings=None)`: Initialize with a list of floats. If `None`, use an empty list.

## Task 2: Implement Collection Protocol
- Implement `__len__(self)`: Return the count of readings.
- Implement `__getitem__(self, index)`: Return the reading at the given index.
- Implement `__iter__(self)`: Allow iterating over the readings.

## Task 3: Implement `__sub__`
- Implement `__sub__(self, other)`.
- Validate `other` is an instance of `VitalHistory`.
- Calculate the average of `self.readings`.
- Calculate the average of `other.readings`.
- Return the difference: `avg_self - avg_other`.
- Handle empty lists by returning `0.0` or raising an error if calculation is impossible.

## Task 4: String Representation
- Implement `__repr__(self)` to return a developer-friendly string like `VitalHistory([98.6, 99.1])`.

## Task 5: Testing
- Create two histories.
- Subtract them and print the trend.
- Iterate through one using a `for` loop.
