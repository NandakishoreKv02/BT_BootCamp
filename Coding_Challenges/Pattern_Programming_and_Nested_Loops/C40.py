def print_factorial_pattern(n):
    """
    Prints a factorial pattern with n rows.

    Args:
        n (int): Number of rows

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    factorial = 1
    num = 1

    for i in range(1, n + 1):
        for _ in range(i):
            factorial *= num
            print(factorial, end=" ")
            num += 1
        print()  # New line after each row


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    print_factorial_pattern(n)
