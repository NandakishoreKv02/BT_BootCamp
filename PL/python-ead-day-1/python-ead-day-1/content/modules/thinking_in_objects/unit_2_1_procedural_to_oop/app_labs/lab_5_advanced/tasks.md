# Lab 5 Tasks

## Task 1: Pharmacy Object
Create `create_pharmacy()`:
- Returns `{'inventory': { 'Amoxicillin': {'stock': 50, 'price': 10} }, 'cash': 0}`.

## Task 2: Patient Object
Create `create_patient(name, cash)`: 
- Returns `{'name': name, 'cash': cash, 'meds': []}`.

## Task 3: Transaction Logic
Create `dispense_medication(pharmacy, patient, drug_name)`:
- Validate drug exists and stock > 0.
- Validate patient cash >= price.
- Perform transaction (update all 4 values).
- Return True/False.

## Task 4: Scenario
- Setup Pharmacy.
- Setup Patient "Alice" ($100).
- Dispense Amoxicillin.
- Dispense ExpensiveMeds (fail due to cost).
- Print logs.
