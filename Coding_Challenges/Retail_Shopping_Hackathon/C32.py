if __name__ == "__main__":
    try:
        total = float(input("Final amount: "))
        if total < 500:
            print("Minimum purchase of ₹500 not met")
        else:
            print("Invoice generated successfully")
    except ValueError:
        print("Invalid input")
