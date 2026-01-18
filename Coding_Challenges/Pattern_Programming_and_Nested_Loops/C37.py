def print_number_increasing_pattern(n):
    """
    Prints a number increasing pattern with n rows.

    Args:
        n (int): Number of rows

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()  # New line after each row


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    print_number_increasing_pattern(n)
