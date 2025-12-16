def number_to_words(num):
    """
    Converts a number into words using mathematical logic.

    Args:
        num (int): Input number

    Raises:
        ValueError: If number is negative
    """
    if num < 0:
        raise ValueError("Number must be non-negative")

    digit_words = [
        "Zero", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine"
    ]

    if num == 0:
        print("Zero")
        return

    digits = []

    while num > 0:
        digits.append(num % 10)
        num //= 10

    # Reverse digits to maintain order
    for digit in reversed(digits):
        print(digit_words[digit], end=" ")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    number_to_words(number)
