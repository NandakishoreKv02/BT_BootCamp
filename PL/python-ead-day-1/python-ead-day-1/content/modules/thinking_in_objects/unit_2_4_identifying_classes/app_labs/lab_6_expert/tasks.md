# Lab 6 Tasks

## Task 1: Identify the Entities
Create the following classes:
- `Patient`: `__init__(self, name)` and `self.is_checked_in = False`.
- `Procedure`: `__init__(self, description, cost)`.
- `OperatingRoom`: `__init__(self, room_id)` and `self.is_reserved = False`.
- `InsuranceClaim`: `__init__(self, patient_obj, cost)`.

## Task 2: Implement the Workflow Controller
Create `SurgeryController`.
- Define `schedule_surgery(self, patient, proc, room)`:
  - Print a planning message.
  - Set `room.is_reserved = True`.
- Define `generate_billing(self, patient, proc)`:
  - If `patient.is_checked_in` is False, return None (cannot bill yet).
  - Else, return a new `InsuranceClaim` object.

## Task 3: The Check-in Trigger
Add a method `check_in(self, patient)` to `SurgeryController` (or another class) that sets the patient's flag to `True`.

## Task 4: Complete Simulation
In `main()`:
1. Initialize the Surgeon, Patient, Procedure, and Operating Room.
2. Run the scheduling logic.
3. Attempt to generate billing BEFORE check-in (Verify it fails).
4. Perform check-in.
5. Generate billing (Verify it succeeds).
6. Print the details of the final insurance claim.
