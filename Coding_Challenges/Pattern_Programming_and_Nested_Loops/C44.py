def reverse_number(num):
    """
    Reverses a given integer number using mathematical logic.

    Args:
        num (int): Input number

    Returns:
        int: Reversed number
    """
    reverse = 0
    n = abs(num)

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return -reverse if num < 0 else reverse


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    reversed_number = reverse_number(number)

    print("Reversed number:", reversed_number)
