# Lab 3 Tasks

## Task 1: Ambulance Class
- Implement `Ambulance` with `id` and `is_available`.
- Add assignment/completion methods.

## Task 2: Dispatcher Class
- Implement `Dispatcher` which holds a list of Ambulance objects.
- Implement `dispatch_to_emergency(location)` which iterates the list finding a free unit.

## Task 3: Simulating the Shift
In `main()`:
1. Create a Dispatcher with 2 ambulances.
2. Request 3 dispatches (One should fail).
3. Complete a mission for Unit 1.
4. Request another dispatch (Should succeed now).
