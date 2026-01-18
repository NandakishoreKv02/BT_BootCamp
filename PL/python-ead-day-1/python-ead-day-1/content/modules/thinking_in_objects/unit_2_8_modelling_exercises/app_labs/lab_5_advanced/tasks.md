# Lab 5 Tasks

## Task 1: Initialize the Many-to-Many Classes
- `Clinic`: Initialize `self.staff = []`.
- `Specialist`: Initialize `self.clinics = []`.

## Task 2: Implement the Onboarding logic
In `Clinic`, implement `onboard_specialist(self, specialist_obj)`:
1. Append the specialist to `self.staff`.
2. Append `self` (the clinic object) to `specialist_obj.clinics`.

## Task 3: Multi-site Simulation
In `main()`:
1. Create "Dr. House".
2. Create "Princeton Clinic" and "Mercy Hospital".
3. Onboard Dr. House to both.
4. Print his list of active locations to verify he is registered at both sites.
