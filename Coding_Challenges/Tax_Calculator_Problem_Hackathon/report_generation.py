def generate_report(details):
    print("\n========== Employee Tax Report ==========")
    print(f"{'Field':<25} {'Value':>15}")
    print("-" * 40)

    print(f"{'Employee Name':<25} {details['name']:>15}")
    print(f"{'Employee ID':<25} {details['emp_id']:>15}")
    print(f"{'Gross Monthly Salary':<25} ₹{details['gross_monthly']:>14.2f}")
    print(f"{'Annual Gross Salary':<25} ₹{details['annual_gross']:>14.2f}")
    print(f"{'Taxable Income':<25} ₹{details['taxable_income']:>14.2f}")
    print(f"{'Tax Payable (incl. cess)':<25} ₹{details['total_tax']:>14.2f}")
    print(f"{'Annual Net Salary':<25} ₹{details['net_salary']:>14.2f}")

    print("=" * 40)

