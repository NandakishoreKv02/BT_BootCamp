# Lab 5 Tasks

## Task 1: The Heart (Entities)
Create a `Patient` class.

## Task 2: The Skin (Boundary)
Create a `RegistrationUI`.
- Define `get_form_data(self)`: Return a dictionary with hardcoded or mocked data (name/mrn).
- Define `show_message(self, text)`: Print the text.

## Task 3: The Brain (Controller)
Create `RegistrationController`.
- Store a list of `patients`.
- Define `validate(self, mrn)`: Return `True` if `len(mrn) == 4`.
- Define `handle_registration(self, name, mrn)`:
  - Call `validate()`.
  - If true, create `Patient` object and add to list.
  - Return the created object or None.

## Task 4: The BCE Orchestration
In `main()`:
1. Initialize all three classes.
2. Get data from the UI.
3. Pass data to the Controller for processing.
4. Pass the result back to the UI for display.
