# Lab 3: Patient Appointment Scheduler - Tasks

## Task 1: Schedule Initialization
Create `create_schedule()` - Return empty dict

## Task 2: Availability Check
Create `is_slot_available(schedule, time)` - Return True if time not in schedule or value is None

## Task 3: Booking Logic
Create `book_appointment(schedule, time, patient_name)` - Check availability, add to schedule, return success boolean

## Task 4: Cancellation
Create `cancel_appointment(schedule, time)` - Set time slot to None or remove from dict

## Task 5: Display
Create `display_schedule(schedule)` - Print formatted schedule with available slots marked

## Task 6: File Persistence
Create `save_schedule(schedule, filename)` and `load_schedule(filename)` - Use file I/O with error handling
