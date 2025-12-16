STANDARD_DEDUCTION = 50000

def calculate_taxable_income(annual_gross_salary):
    taxable_income = max(annual_gross_salary - STANDARD_DEDUCTION, 0)

    print(f"Gross Salary: ₹{annual_gross_salary}")
    print(f"Standard Deduction: ₹{STANDARD_DEDUCTION}")
    print(f"Taxable Income: ₹{taxable_income}")

    return taxable_income
