# Lab 3 Tasks

## Task 1: Create the `Observer` Interface
- Define an abstract class `Observer`.
- Add an `@abstractmethod` called `update(self, alert_msg)`.

## Task 2: Implement the `Subject` Class
- Attributes: `self._observers` (list).
- Method `attach(self, observer)`: Adds to list.
- Method `detach(self, observer)`: Removes from list.
- Method `notify(self, message)`: Loops through all observers and calls their `update` method.

## Task 3: build `VitalMonitor` (Concrete Subject)
- Class `VitalMonitor` inherits from `Subject`.
- Method `check_vitals(self, patient_name, heart_rate)`: 
    - If HR > 120, call `self.notify(f"TACTICAL ALERT: {patient_name} HR at {heart_rate}")`.

## Task 4: implement Concrete Observers
- `NurseStation`: Prints "Nurse Alert: {msg}".
- `EmergencySystem`: Prints "CODE BLUE TRIGGERED: {msg}".

## Task 5: test Integration
- Create one monitor.
- Attach the nurse station.
- Trigger an alert and verify the nurse sees it.
- Attach the emergency system and trigger another alert.
