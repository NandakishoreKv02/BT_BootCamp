# Lab 5 Tasks

## Task 1: Initialize the Multi-Reference Classes
- `Nurse`: Initialize `self.depts = []`.
- `Department`: Initialize `self.staff = []`.

## Task 2: Implement the M:N Interaction
In `Nurse`, implement `assign_to_department(self, dept_obj)`:
1. Check if the department is already in `self.depts`. If so, return.
2. Append `dept_obj` to `self.depts`.
3. Append `self` to `dept_obj.staff`.

## Task 3: The workforce loop
In `main()`:
1. Create two nurses (N1, N2).
2. Create two departments (D1, D2).
3. Assign N1 to both D1 and D2.
4. Assign N2 to only D2.
5. Print the roster for D2 and the schedule for N1.
