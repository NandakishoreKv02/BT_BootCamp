# Lab 5 Tasks

## Task 1: Protocol Strategies
- `CardiacStrategy`: Method `execute()` returns "Applying Defibrillator Protocol".
- `TraumaStrategy`: Method `execute()` returns "Applying Pressure/Stabilization Protocol".

## Task 2: The Strategy Factory
- Class `ProtocolFactory`.
- Map "cardiac" -> `CardiacStrategy`.
- Map "trauma" -> `TraumaStrategy`.

## Task 3: The Manager
- `PatientManager`.
- `__init__(self, patient_name)`.
- Method `set_condition(self, condition_str)`:
    - Uses `ProtocolFactory` to get the strategy.
    - Sets `self.active_protocol`.
- Method `treat(self)`: Calls `self.active_protocol.execute()`.

## Task 4: Advanced Validation
- Ensure that if the factory gets an unknown condition, it returns a `DefaultStrategy` (which returns "General Observation").
