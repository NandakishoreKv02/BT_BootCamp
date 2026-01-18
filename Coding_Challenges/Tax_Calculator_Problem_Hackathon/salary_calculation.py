def calculate_salary(basic_salary, special_allowance, bonus_percent):
    gross_monthly_salary = basic_salary + special_allowance
    annual_bonus = (gross_monthly_salary * 12 * bonus_percent) / 100
    annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus
    return gross_monthly_salary, annual_bonus, annual_gross_salary
