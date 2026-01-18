def print_number_pattern(n):
    """
    Prints a number pattern with n rows.
    Each row contains numbers from 1 to 5.

    Args:
        n (int): Number of rows

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    for _ in range(n):
        for num in range(1, 6):
            print(num, end="")
        print()  # Move to next line


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    print_number_pattern(n)
