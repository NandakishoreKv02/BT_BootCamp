def print_fibonacci_pattern(n):
    """
    Prints a Fibonacci series pattern with n rows.

    Args:
        n (int): Number of rows

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    a, b = 1, 1

    for i in range(1, n + 1):
        for _ in range(i):
            print(a, end=" ")
            a, b = b, a + b
        print()  # New line after each row


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    print_fibonacci_pattern(n)
