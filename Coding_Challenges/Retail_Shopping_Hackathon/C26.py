def calculate_item_total(quantity, price):
    return quantity * price


if __name__ == "__main__":
    try:
        grand_total = 0
        n = int(input("Enter number of items: "))

        for i in range(n):
            print(f"\nItem {i+1}")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            item_total = calculate_item_total(qty, price)
            grand_total += item_total

        print("\nGrand Total: ₹", grand_total)
    except ValueError:
        print("Invalid input")
