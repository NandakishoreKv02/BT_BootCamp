# Lab 4 Tasks

## Task 1: Create the Strategy Interface
- Define an abstract class `RiskStrategy`.
- Add an `@abstractmethod` called `calculate_risk(self, readings)`.

## Task 2: Implement Concrete Strategies
- `AdultStrategy`: Returns "HIGH" if HR > 100.
- `PediatricStrategy`: Returns "HIGH" if HR > 140.

## Task 3: Implement the Context Class
- Define class `PatientRiskAssessor`.
- `__init__(self, strategy)`.
- Method `set_strategy(self, strategy)`.
- Method `assess(self, heart_rate)`: Calls `self.strategy.calculate_risk(heart_rate)`.

## Task 4: implementation
- Create the assessor with the Adult strategy.
- Assess a heart rate of 110 (Should be HIGH).
- Switch to the Pediatric strategy.
- Assess 110 again (Should be NORMAL).
