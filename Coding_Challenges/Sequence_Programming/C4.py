def swap_numbers(a, b):
    """
    Swaps two numbers.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        tuple: Swapped values (b, a)
    """
    return b, a


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    x, y = swap_numbers(x, y)

    print("After swapping:")
    print("First number:", x)
    print("Second number:", y)
