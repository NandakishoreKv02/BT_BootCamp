def calculate_sum_and_average(a, b):
    """
    Calculates the sum and average of two numbers.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        tuple: (sum, average)

    Raises:
        TypeError: If inputs are not numeric
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")

    total = a + b
    average = total / 2
    return total, average


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    total, avg = calculate_sum_and_average(x, y)
    print(f"Sum: {total}")
    print(f"Average: {avg}")
