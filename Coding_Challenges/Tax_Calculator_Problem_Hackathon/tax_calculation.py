def calculate_tax(taxable_income):
    tax = 0
    breakdown = []

    slabs = [
        ("0 – 3,00,000", 300000, 0),
        ("3,00,001 – 6,00,000", 300000, 0.05),
        ("6,00,001 – 9,00,000", 300000, 0.10),
        ("9,00,001 – 12,00,000", 300000, 0.15),
        ("12,00,001 – 15,00,000", 300000, 0.20),
        ("Above 15,00,000", float('inf'), 0.30)
    ]

    remaining_income = taxable_income

    for name, slab_amount, rate in slabs:
        if remaining_income <= 0:
            break
        taxable_part = min(remaining_income, slab_amount)
        slab_tax = taxable_part * rate
        breakdown.append((name, taxable_part, rate, slab_tax))
        tax += slab_tax
        remaining_income -= taxable_part

    # Section 87A Rebate
    if taxable_income <= 700000:
        tax = 0

    cess = tax * 0.04
    total_tax = tax + cess

    # Display breakdown
    print(f"Taxable Income: ₹{taxable_income}")
    print("\nTax Breakdown:")
    for slab, amount, rate, slab_tax in breakdown:
        print(f"{slab}: ₹{amount} @ {rate*100}% = ₹{slab_tax}")

    print(f"\nTax after rebate: ₹{tax}")
    print(f"Health & Education Cess (4%): ₹{cess}")
    print(f"Total Tax Payable: ₹{total_tax}")

    return tax, cess, total_tax
