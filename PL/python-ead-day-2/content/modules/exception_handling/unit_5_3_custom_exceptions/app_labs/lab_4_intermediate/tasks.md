# Lab 4 Tasks

## Task 1: Custom Exception
- Define `DrugInteractionError(Exception)`.

## Task 2: Dispense Logic
- Implement `dispense_medication(drug_name, quantity)`.
- If `quantity` is not an `int`, raise `TypeError("Quantity must be a number")`.
- If `drug_name` is in a "forbidden" list (let's use `["Warfarin", "Aspirin"]` together for the simulation, or just flag `"ForbiddenDrug"`), raise `DrugInteractionError`.
- Let's say if drug is `"Statin"` and quantity > 10, it's a `ValueError` (business rule but generic). Actually, let's keep it simple:
    - Non-int -> `TypeError`.
    - `"Incompatible"` -> `DrugInteractionError`.
    - Otherwise -> return `"Dispensed"`.

## Task 3: Reporting
- Implement `process_order(drug, qty)`.
- Catch `TypeError`: return "System Error: Bad Input".
- Catch `DrugInteractionError`: return "Medical Alert: Safety Violation".
- Catch others: return "Generic Error".
