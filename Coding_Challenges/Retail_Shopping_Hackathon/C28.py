def apply_membership_discount(total, is_member):
    """
    Applies membership discount if applicable.
    """
    if is_member.lower() == 'y':
        total *= 0.98
    return total


if __name__ == "__main__":
    try:
        total = 0
        qty_sum = 0
        n = int(input("Number of items: "))

        for _ in range(n):
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            total += qty * price
            qty_sum += qty

        if total > 10000:
            total *= 0.90
        if qty_sum > 20:
            total *= 0.95

        member = input("Are you a member? (y/n): ")
        total = apply_membership_discount(total, member)

        print("Total after membership discount: ₹", round(total, 2))
    except ValueError:
        print("Invalid input")
