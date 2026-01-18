def check_even_or_odd(number):
    """
    Checks whether a number is even or odd.

    Args:
        number (int): Input number

    Returns:
        str: "Even" or "Odd"

    Raises:
        ValueError: If input is not an integer
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check_even_or_odd(num)
    print(f"The number is {result}")
