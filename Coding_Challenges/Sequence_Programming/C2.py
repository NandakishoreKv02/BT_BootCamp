def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest.

    Args:
        principal (int or float): Principal amount
        rate (int or float): Rate of interest
        time (int or float): Time period

    Returns:
        float: Simple interest

    Raises:
        TypeError: If inputs are not numeric
        ValueError: If inputs are negative
    """
    for value in (principal, rate, time):
        if not isinstance(value, (int, float)):
            raise TypeError("Principal, rate, and time must be numbers")
        if value < 0:
            raise ValueError("Principal, rate, and time cannot be negative")

    simple_interest = (principal * rate * time) / 100
    return simple_interest


if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time period: "))

    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest: {si}")
