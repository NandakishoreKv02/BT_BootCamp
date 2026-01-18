# Lab 3 Tasks

## Task 1: The Domain Entities
- Create `Patient` (`name`).
- Create `Physician` (`name`).

## Task 2: The Linking Object
Create `TimeSlot` class.
- `__init__(self, time_str)`:
  - Store the time string.
  - Set `self.booked_to = None` (**Aggregation**).
  - Set `self.assigned_dr = None` (**Aggregation**).

## Task 3: The Container (Composition)
Create `DailySchedule` class.
- `__init__(self, date_str, slots_list)`:
  - Store the date.
  - Create a list `self.slots` containing new `TimeSlot` objects for each string in `slots_list`.
- Implement `schedule_appointment(self, time_index, patient_obj, dr_obj)`:
  - Find the slot at the given index.
  - Link the patient and doctor objects to it.
