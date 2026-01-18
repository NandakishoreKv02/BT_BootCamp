# Lab 4 Tasks

## Task 1: Define ABC `MedicalDevice`
- Inherit from `ABC`.
- Define abstract method `connect(self)`.
- Define abstract method `get_status(self)`.

## Task 2: Implement `InfusionPump`
- Inherit from `MedicalDevice`.
- `connect`: Print "Pump connecting..." and return `True`.
- `get_status`: Return dictionary `{"battery": 95, "drug_remaining": 50}`.

## Task 3: Test Non-Compliant Class
- Define class `BadDevice(MedicalDevice)` that implements nothing.
- Try to instantiate it and catch the `TypeError`.

## Task 4: Integration
- Write a function `diagnose(device: MedicalDevice)` that calls `get_status()` and prints it.
