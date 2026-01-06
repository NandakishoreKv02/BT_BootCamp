def calculate_item_total(code, description, quantity, price):
    """
    Calculates total cost for a single item.

    Args:
        code (str): Item code
        description (str): Item description
        quantity (int): Quantity purchased
        price (float): Price per unit

    Returns:
        float: Total cost for the item

    Raises:
        ValueError: If quantity or price is invalid
    """
    if quantity <= 0 or price <= 0:
        raise ValueError("Quantity and price must be positive")

    return quantity * price


if __name__ == "__main__":
    try:
        code = input("Item Code: ")
        desc = input("Description: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))

        total = calculate_item_total(code, desc, qty, price)
        print("Item Total: ₹", total)
    except ValueError as e:
        print("Error:", e)
