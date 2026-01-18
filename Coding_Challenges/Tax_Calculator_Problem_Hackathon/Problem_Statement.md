# Tax Calculator Problem — Hackathon

**GlobalNext Solutions** aims to streamline tax calculation for employees under the **New Tax Regime (2023)**. The HR-Tech team needs a program that processes employee salary details, validates inputs, calculates taxes and net incomes, and produces readable reports.

---

## Overview

The program must:

- Accept employee details including monthly salary components.
- Calculate gross and taxable income according to the New Tax Regime (2023).
- Compute tax payable using the appropriate tax slabs.
- Apply standard deductions and rebates.
- Generate reports detailing gross salary, taxable income, tax payable, and net salary.

---

## Coding Challenge 11 — Basic Input and Salary Calculation ✅

**Objective:** Capture employee details and calculate gross salary.

**Inputs:**
- Name
- EmpID
- Basic Monthly Salary
- Special Allowances (Monthly)
- Bonus Percentage (Annual bonus as % of gross salary)

**Calculate:**
- Gross Monthly Salary = Basic Salary + Special Allowances
- Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus

**Output:** Display employee details, gross monthly salary, and annual gross salary.

---

## Coding Challenge 12 — Taxable Income Calculation 🔧

**Objective:** Calculate taxable income after standard deduction.

**Tasks:**
- Deduct a **Standard Deduction of ₹50,000** from the annual gross salary.
- Compute Taxable Income and display intermediate calculations.

**Output:** Gross salary, standard deduction, and taxable income.

---

## Coding Challenge 13 — Tax and Rebate Calculation 💡

**Objective:** Compute tax payable using the New Tax Regime (2023).

**Tax Slabs (annual taxable income):**

| Range (₹) | Rate |
|-----------:|:----:|
| 0 – 3,00,000 | 0% |
| 3,00,001 – 6,00,000 | 5% |
| 6,00,001 – 9,00,000 | 10% |
| 9,00,001 – 12,00,000 | 15% |
| 12,00,001 – 15,00,000 | 20% |
| Above 15,00,000 | 30% |

**Additional rules:**
- **Section 87A Rebate:** If Taxable Income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
- Add **4% Health and Education Cess** to the calculated tax.

**Output:** Detailed tax breakdown (tax per slab), cess, rebates applied, and total tax payable.

---

## Coding Challenge 14 — Net Salary Calculation 🧾

**Objective:** Calculate annual net salary after tax deductions.

**Tasks:**
- Net Salary = Annual Gross Salary − Total Tax Payable (including cess)

**Output:** Annual Gross Salary, Total Tax Payable (including cess), Annual Net Salary.

---

## Coding Challenge 15 — Report Generation 📋

**Objective:** Generate a detailed, readable report for employees.

**Report should include:**
- Employee Details (Name, EmpID)
- Gross Monthly Salary
- Annual Gross Salary
- Taxable Income
- Tax Payable (with breakdown: slab-wise tax, rebate, cess)
- Annual Net Salary

**Presentation:** Provide a clean, tabular report for readability.

**Example Report (sample values):**

| Field | Details |
|---|---:|
| Name | John Doe |
| EmpID | E12345 |
| Gross Monthly Salary | ₹85,000 |
| Annual Gross Salary | ₹10,20,000 |
| Taxable Income | ₹9,70,000 |
| Tax Payable (incl. cess) | ₹76,800 |
| Annual Net Salary | ₹9,43,200 |

---

## Coding Challenge 16 — Input Validation Rules ⚠️

**Objective:** Validate inputs for accuracy and correctness.

**Validation rules:**
1. Employee Details
   - Name: Non-empty, alphabets only, maximum 50 characters.
   - EmpID: Alphanumeric, 5–10 characters.
2. Salary Inputs
   - Basic Salary: Positive number, max ₹1,00,00,000.
   - Special Allowances: Non-negative, max ₹1,00,00,000.
   - Bonus Percentage: Numeric value, 0–100.
3. Derived Calculations
   - Gross Monthly Salary must be > 0.
   - Annual Gross Salary should be within realistic bounds.
4. General
   - Reject invalid inputs with a clear error message and prompt for re-entry.

**Output:** Indicate invalid inputs clearly and prompt for correction.

---

## Notes & Implementation Tips 💡

- Keep functions small: one to read/validate inputs, one to compute salary and tax, and one to render the report.
- Include unit tests for tax slab calculations and validation rules.
- Consider edge cases: incomes exactly on slab boundaries, 0 salary, and rebate applicability.

