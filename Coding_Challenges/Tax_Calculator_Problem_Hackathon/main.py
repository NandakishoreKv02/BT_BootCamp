from input_validation import *
from salary_calculation import calculate_salary
from taxable_income import calculate_taxable_income
from tax_calculation import calculate_tax
from net_salary import calculate_net_salary
from report_generation import generate_report

# Input Section
while True:
    try:
        name = input("Enter Employee Name: ")
        emp_id = input("Enter Employee ID: ")

        basic_salary = float(input("Enter Basic Monthly Salary: "))
        special_allowance = float(input("Enter Special Allowance: "))
        bonus_percent = float(input("Enter Bonus Percentage: "))

        if not validate_name(name):
            raise ValueError("Invalid Name")
        if not validate_emp_id(emp_id):
            raise ValueError("Invalid EmpID")
        if not validate_basic_salary(basic_salary):
            raise ValueError("Invalid Basic Salary")
        if not validate_allowance(special_allowance):
            raise ValueError("Invalid Special Allowance")
        if not validate_bonus(bonus_percent):
            raise ValueError("Invalid Bonus Percentage")

        break  # All inputs valid

    except ValueError as e:
        print(e)
        print("Please re-enter all details.\n")


# Calculations
gross_monthly, bonus, annual_gross = calculate_salary(
    basic_salary, special_allowance, bonus_percent
)

taxable_income = calculate_taxable_income(annual_gross)
tax, cess, total_tax = calculate_tax(taxable_income)
net_salary = calculate_net_salary(annual_gross, total_tax)

# Report
generate_report({
    "name": name,
    "emp_id": emp_id,
    "gross_monthly": gross_monthly,
    "annual_gross": annual_gross,
    "taxable_income": taxable_income,
    "total_tax": total_tax,
    "net_salary": net_salary
})
