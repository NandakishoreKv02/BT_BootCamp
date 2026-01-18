# Lab 6 Tasks

## Task 1: Define `AlertStrategy` ABC
- Methods: `evaluate(self, data: list)` -> returns `True` if alert needed.

## Task 2: Implement `ThresholdStrategy`
- Accepts `limit` in `__init__`.
- `evaluate` returns `True` if any value in data > `limit`.

## Task 3: Implement `AverageStrategy`
- Accepts `limit` in `__init__`.
- `evaluate` returns `True` if `sum(data)/len(data)` > `limit`.

## Task 4: Create `PatientMonitor`
- `__init__(self, patient_name, strategy: AlertStrategy)`.
- Method `add_data(self, value)`: Append reading.
- Method `check_status(self)`: Call `self.strategy.evaluate(self.data)` and return the result.

## Task 5: Polymorphism Test
- Create one monitor with `ThresholdStrategy`.
- Create another with `AverageStrategy`.
- Feed both the same data (some high spikes, low average) and observe different alerts.
