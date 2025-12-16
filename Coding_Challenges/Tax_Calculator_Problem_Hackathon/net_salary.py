def calculate_net_salary(annual_gross_salary, total_tax):
    net_salary = annual_gross_salary - total_tax

    print(f"Annual Gross Salary: ₹{annual_gross_salary}")
    print(f"Total Tax Payable (including cess): ₹{total_tax}")
    print(f"Annual Net Salary: ₹{net_salary}")

    return net_salary

