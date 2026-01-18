# Lab 4 Tasks

## Task 1: Policy Rule Functions
Define three logic functions that return `True` (Admit) or `False` (Deny):
- `general_policy(ward, patient)`: Only checks if `occupied < total`.
- `icu_policy(ward, patient)`: Space exists AND `patient['priority'] == 'High'`.
- `peds_policy(ward, patient)`: Space exists AND `patient['age'] < 18`.

## Task 2: The Scalable Admission Engine
Define `admit_to_ward(ward, patient, policy_map)`:
- Look up the policy function in the `policy_map` using the `ward['type']`.
- If no policy exists for that type, return `False`.
- Execute the found policy function.
- If it returns `True`, increment `ward['occupied']`.
- Return the final result.

## Task 3: Setup and Calibration
1. Create ward dictionaries (e.g., ICU-A with type "ICU").
2. Create `policies = {"General": general_policy, "ICU": icu_policy, ...}`.
3. Test with various patients:
   - High Priority patient into ICU.
   - Low Priority patient into ICU.
   - Adult into Pediatrics.

## Task 4: Proving Scalability
Add a `vip_policy(ward, patient)` that checks for a `vip` flag. Add it to the `policies` map and demonstrate it works without you having to re-write or touch the `admit_to_ward` engine.
