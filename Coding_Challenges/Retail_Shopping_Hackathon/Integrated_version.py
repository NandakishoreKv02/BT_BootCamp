def calculate_item_total(code, quantity, price):
    """
    Calculates item total with promotional discount if applicable.

    Args:
        code (str): Item code
        quantity (int): Quantity purchased
        price (float): Price per unit

    Returns:
        float: Final item total after promo discount
    """
    total = quantity * price

    # Promotional discount
    if code.upper() == "PROMO10":
        total *= 0.90  # 10% off

    return total


def apply_discounts(grand_total, total_quantity):
    """
    Applies discount rules based on total amount and quantity.

    Args:
        grand_total (float): Total before discounts
        total_quantity (int): Total quantity of all items

    Returns:
        float: Discounted total
    """
    if grand_total > 10000:
        grand_total *= 0.90  # 10% discount

    if total_quantity > 20:
        grand_total *= 0.95  # Additional 5% discount

    return grand_total


def apply_membership_discount(total, is_member):
    """
    Applies membership discount.

    Args:
        total (float): Amount after normal discounts
        is_member (str): 'y' or 'n'

    Returns:
        float: Updated total
    """
    if is_member.lower() == 'y':
        total *= 0.98  # 2% discount
    return total


def calculate_tax(total):
    """
    Calculates tax based on slab.

    Args:
        total (float): Amount before tax

    Returns:
        float: Tax amount
    """
    if total < 5000:
        return total * 0.05
    elif total <= 20000:
        return total * 0.10
    else:
        return total * 0.15


def apply_payment_surcharge(total, mode):
    """
    Applies surcharge based on payment method.

    Args:
        total (float): Amount after tax
        mode (str): cash or credit

    Returns:
        float: Final payable amount
    """
    if mode.lower() == "credit":
        return total * 1.02  # 2% surcharge
    return total


def calculate_loyalty_points(total):
    """
    Calculates loyalty points.

    Args:
        total (float): Final payable amount

    Returns:
        int: Loyalty points earned
    """
    return int(total // 100)


# ---------------- MAIN PROGRAM ---------------- #

if __name__ == "__main__":
    try:
        print("\n--- Retail Shopping Application ---")

        n = int(input("Enter number of items: "))
        if n <= 0:
            raise ValueError("At least one item must be purchased")

        grand_total = 0
        total_quantity = 0
        invoice_items = []

        for i in range(n):
            print(f"\nItem {i + 1}")
            code = input("Item Code: ")
            desc = input("Description: ")
            qty = int(input("Quantity: "))
            price = float(input("Price per unit: "))

            if qty <= 0 or price <= 0:
                raise ValueError("Quantity and price must be positive")

            item_total = calculate_item_total(code, qty, price)

            invoice_items.append((code, desc, qty, price, item_total))
            grand_total += item_total
            total_quantity += qty

        # Apply discounts
        grand_total = apply_discounts(grand_total, total_quantity)

        # Membership
        member = input("\nAre you a member? (y/n): ")
        grand_total = apply_membership_discount(grand_total, member)

        # Tax
        tax = calculate_tax(grand_total)
        grand_total += tax

        # Payment
        payment_mode = input("Payment mode (cash/credit): ")
        grand_total = apply_payment_surcharge(grand_total, payment_mode)

        # Minimum purchase check
        if grand_total < 500:
            print("\nMinimum purchase of ₹500 not met. Invoice cannot be generated.")
            exit()

        # Loyalty points
        points = calculate_loyalty_points(grand_total)

        # -------- Invoice -------- #
        print("\n========== INVOICE ==========")
        for item in invoice_items:
            print(f"{item[1]} ({item[0]}) | Qty: {item[2]} | Price: ₹{item[3]} | Total: ₹{round(item[4], 2)}")

        print("-----------------------------")
        print("Tax Applied: ₹", round(tax, 2))
        print("Payment Mode:", payment_mode.capitalize())
        print("Final Payable Amount: ₹", round(grand_total, 2))
        print("Loyalty Points Earned:", points)
        print("========== THANK YOU ==========")

    except ValueError as e:
        print("Error:", e)
