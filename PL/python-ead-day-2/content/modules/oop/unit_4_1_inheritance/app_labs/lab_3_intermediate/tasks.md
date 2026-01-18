# Lab 3 Tasks

## Task 1: `Staff` Base Pay
- Define `Staff` with a `base_salary` attribute (default 50000).
- Implement `calculate_pay()` returning `self.base_salary`.

## Task 2: `MedicalStaff` Hazard Pay
- Create `MedicalStaff` inheriting from `Staff`.
- Override `calculate_pay()`.
- Use `super().calculate_pay()` to get the base amount.
- Add 10000 to it and return the total.

## Task 3: `Surgeon` Operation Bonus
- Create `Surgeon` inheriting from `MedicalStaff`.
- Override `calculate_pay()`.
- Use `super().calculate_pay()` to get the (Hazard + Base) amount.
- Add 30000 to it and return the total.

## Task 4: Verify
- Create instances of each class.
- Assert their final pay is 50k, 60k, and 90k respectively.
