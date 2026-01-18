# Lab 1 Tasks

## Task 1: Create the Singleton Structure
- Define a class `SystemConfig`.
- Use a class variable `_instance = None`.
- Override `__new__(cls)`.
- If `_instance` is None, initialize it using `super().__new__(cls)`.

## Task 2: Implement Threshold Management
- In `__init__`, initialize a dictionary `self.thresholds` if it doesn't already exist.
- Method `set_threshold(self, vital_name, value)`.
- Method `get_threshold(self, vital_name)`.

## Task 3: verification
- Instantiate `config1 = SystemConfig()`.
- Instantiate `config2 = SystemConfig()`.
- Print `config1 is config2` to verify identity.

## Task 4: Global Consistency
- Set a threshold in `config1`.
- Retrieve it from `config2` and ensure it matches.
