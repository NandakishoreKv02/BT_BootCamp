def calculate_discount(total_amount, discount_percent):
    """
    Calculates discount amount and final payable amount.

    Args:
        total_amount (float): Total purchase amount
        discount_percent (float): Discount percentage

    Returns:
        tuple: (discount_amount, final_amount)

    Raises:
        ValueError: If inputs are negative
    """
    if total_amount < 0 or discount_percent < 0:
        raise ValueError("Total amount and discount percentage cannot be negative")

    discount_amount = (total_amount * discount_percent) / 100
    final_amount = total_amount - discount_amount

    return discount_amount, final_amount


if __name__ == "__main__":
    total = float(input("Enter total amount: "))
    discount = float(input("Enter discount percentage: "))

    discount_amt, final_amt = calculate_discount(total, discount)

    print(f"Discount Amount: {discount_amt}")
    print(f"Final Payable Amount: {final_amt}")
