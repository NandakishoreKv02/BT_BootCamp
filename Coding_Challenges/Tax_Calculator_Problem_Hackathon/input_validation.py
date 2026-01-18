import re

def validate_name(name):
    return bool(name) and name.isalpha() and len(name) <= 50

def validate_emp_id(emp_id):
    return bool(re.match(r'^[A-Za-z0-9]{5,10}$', emp_id))

def validate_basic_salary(value, max_value=10000000):
    return value > 0 and value <= max_value

def validate_allowance(value, max_value=10000000):
    return value >= 0 and value <= max_value

def validate_bonus(bonus):
    return 0 <= bonus <= 100

def validate_gross_monthly(value):
    return value > 0

def validate_annual_gross(value, max_value=200000000):
    return value > 0 and value <= max_value
