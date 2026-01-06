def apply_payment_surcharge(total, mode):
    """
    Applies surcharge based on payment mode.
    """
    if mode.lower() == "credit":
        return total * 1.02
    return total


if __name__ == "__main__":
    try:
        total = float(input("Enter total amount: "))
        mode = input("Payment mode (cash/credit): ")
        total = apply_payment_surcharge(total, mode)
        print("Final Payable Amount: ₹", round(total, 2))
    except ValueError:
        print("Invalid input")
