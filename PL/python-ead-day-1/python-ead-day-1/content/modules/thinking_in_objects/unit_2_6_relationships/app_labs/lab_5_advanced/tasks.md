# Lab 5 Tasks

## Task 1: The Permanent Parts (Composition)
Create `Camera` and `MechanicalArm` classes.
- Camera stores `resolution`.
- Arm stores `precision`.

## Task 2: The External Resources (Dependency)
Create `PowerSource` (`source_type`) and `Organ` (`name`).

## Task 3: Assemble the Robot
Create `SurgicalRobot`.
- `__init__(self)`:
  - Create a `Camera` and a `MechanicalArm`.
- `operate(self, power, organ)`:
  - Verify power source.
  - Print that the incision is starting on the organ.
  - Use the precision of the mechanical arm in the message.

## Task 4: Run the Procedure
In `main()`:
1. Initialize the robot.
2. Initialize an external power grid and a patient's kidney.
3. Call the `operate` method.
