# Lab 4: Electronic Health Record (EHR) Stub - Tasks

## Task 1: Addition
In `add_patient`, assign a new key-value pair to the dictionary. 
The key is `mrn`. The value is another dictionary: `{"name": name, "status": status}`.

## Task 2: Retrieval
In `get_patient_status`:
- Use the `.get()` method on the `system` dictionary.
- If the patient exists, return the `"status"` value from their sub-dictionary.
- If not found, return the string `"Not Found"`.

## Task 3: Update
In `update_status`:
- Check if the `mrn` exists in the system.
- If it does, update the `"status"` inside that patient's dictionary.
- Return `True` if updated, `False` otherwise.
