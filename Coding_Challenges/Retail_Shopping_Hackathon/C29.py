def calculate_tax(total):
    """
    Calculates tax based on slabs.
    """
    if total < 5000:
        return total * 0.05
    elif total <= 20000:
        return total * 0.10
    else:
        return total * 0.15


if __name__ == "__main__":
    try:
        total = float(input("Enter amount before tax: "))
        tax = calculate_tax(total)
        total += tax
        print("Tax: ₹", round(tax, 2))
        print("Total with tax: ₹", round(total, 2))
    except ValueError:
        print("Invalid input")
