# Lab 3 Tasks

## Task 1: Define `LoggerMixin`
- Create a class `LoggerMixin`.
- Method `log_event(self, event_type, message)`.
- It should print: `[TIMESTAMP] {event_type}: {message}`.
- (For simplicity, timestamp can be a static string or real `datetime.now()`).

## Task 2: Create `PatientFile`
- Inherit from `LoggerMixin`.
- `__init__(self, patient_name)`.
- Method `update_diagnosis(self, new_diag)`:
    - Update `self.diagnosis`.
    - Call `self.log_event("UPDATE", f"Diagnosis changed for {self.patient_name}")`.

## Task 3: Test Multi-Inheritance
- Create a `PatientFile` object.
- Update its diagnosis and verify the logs appear in the console.

## Task 4: Extension
- Add a second Mixin `JSONExportMixin` with a method `export_json(self)` that returns `json.dumps(self.__dict__)`.
- Inherit `PatientFile` from both.
