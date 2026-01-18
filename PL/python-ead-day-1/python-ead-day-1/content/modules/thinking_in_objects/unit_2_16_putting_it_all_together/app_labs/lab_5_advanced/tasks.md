# Lab 5 Tasks

## Task 1: Abstract Base Class
- Define `TrialPhase` inheriting from ABC.
- Implement concrete `enroll(count)`.
- Define abstract `evaluate()`.

## Task 2: Concrete Phases
- Implement `Phase1Safety`.
- Implement `Phase2Efficacy`.
- Ensure they check `self.participants` in their evaluation logic.

## Task 3: Simulation
In `main()`:
1. Create Phase 1, enrol 20 people. Check evaluation.
2. Create Phase 2, enrol 30 people. Check evaluation (should fail).
