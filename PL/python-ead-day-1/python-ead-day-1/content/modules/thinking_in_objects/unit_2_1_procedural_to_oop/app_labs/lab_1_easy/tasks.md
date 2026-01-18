# Lab 1 Tasks

## Task 1: Create the "Constructor"
Define `make_ward(name, capacity)`:
- Returns a dictionary representing the Object.
- Initialize `occupied` to 0.

## Task 2: Refactor Logic
Define `admit_patient(ward)`:
- Check if `occupied < total`.
- If yes, increment.
- If no, print "Ward [Name] is full!".

Define `discharge_patient(ward)`:
- Check if `occupied > 0`.
- If yes, decrement.

## Task 3: Test Independence
In the `main()` function:
1. Create `icu = make_ward("ICU", 5)`
2. Create `general = make_ward("General", 20)`
3. Admit 2 patients to ICU.
4. Admit 5 patients to General.
5. Print the status of both to prove they are separate.
