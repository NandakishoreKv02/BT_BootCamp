def calculate_loyalty_points(total):
    """
    Calculates loyalty points.
    """
    return int(total // 100)


if __name__ == "__main__":
    try:
        total = float(input("Final amount: "))
        points = calculate_loyalty_points(total)
        print("Loyalty Points Earned:", points)
    except ValueError:
        print("Invalid input")
