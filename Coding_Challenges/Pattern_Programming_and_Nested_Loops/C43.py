def separate_whole_and_fraction(value):
    """
    Separates the whole and fractional parts of a float value.

    Args:
        value (float): Input floating-point number

    Returns:
        tuple: (whole_part, fractional_part)
    """
    whole_part = int(value)
    fractional_part = abs(value - whole_part)

    return whole_part, fractional_part


if __name__ == "__main__":
    number = float(input("Enter a double value: "))

    whole, fraction = separate_whole_and_fraction(number)

    print("Whole part:", whole)
    print("Fractional part:", fraction)
