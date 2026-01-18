def check_tax_eligibility(name, salary):
    """
    Checks if an employee is required to pay tax based on salary.

    Args:
        name (str): Employee name
        salary (float): Annual salary

    Returns:
        str: Tax eligibility message

    Raises:
        ValueError: If salary is negative
    """
    if salary < 0:
        raise ValueError("Salary cannot be negative")

    if salary > 300000:
        return f"{name} must pay tax."
    else:
        return f"{name} does not need to pay tax."


if __name__ == "__main__":
    employee_name = input("Enter employee name: ")
    employee_salary = float(input("Enter annual salary: "))

    result = check_tax_eligibility(employee_name, employee_salary)
    print(result)
