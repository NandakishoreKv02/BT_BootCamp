# Lab 6 Tasks

## Task 1: The Private Implementation
- Define `SurgicalRobot`.
- Create private methods:
  - `__check_power(self)`: returns `True`.
  - `__verify_position(self)`: returns `True`.

## Task 2: The Managed State
- `__init__(self)`: Set `self.__arm_extension = 0`.
- Create a read-only `@property` for `arm_extension`.

## Task 3: The Safe Controller
Implement `deploy(self, target_cm)`:
1. Print "Initiating Deployment...".
2. Call `self.__check_power()` and `self.__verify_position()`.
3. If both pass:
   - Set `self.__arm_extension = target_cm`.
   - Print "Robot arm extended."
4. Else:
   - Print "SAFETY LOCK: Check system failure."

## Task 4: The Interface Audit
In `main()`:
1. Create a robot.
2. Call `robot.deploy(50)`.
3. Try to call `robot.__check_power()`. It should fail because the method is private.
