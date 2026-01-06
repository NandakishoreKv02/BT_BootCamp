def promo_discount(code, item_total):
    """
    Applies promotional discount if code matches.
    """
    if code == "PROMO10":
        return item_total * 0.90
    return item_total


if __name__ == "__main__":
    try:
        grand_total = 0
        n = int(input("Number of items: "))

        for _ in range(n):
            code = input("Item Code: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            item_total = promo_discount(code, qty * price)
            grand_total += item_total

        print("Total after promo discounts: ₹", round(grand_total, 2))
    except ValueError:
        print("Invalid input")
