def apply_discounts(grand_total, total_quantity):
    """
    Applies discount rules on the grand total.
    """
    if grand_total > 10000:
        grand_total *= 0.90  # 10% discount

    if total_quantity > 20:
        grand_total *= 0.95  # additional 5%

    return grand_total


if __name__ == "__main__":
    try:
        grand_total = 0
        total_qty = 0
        n = int(input("Enter number of items: "))

        for _ in range(n):
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            grand_total += qty * price
            total_qty += qty

        grand_total = apply_discounts(grand_total, total_qty)
        print("Total after discounts: ₹", round(grand_total, 2))
    except ValueError:
        print("Invalid input")
