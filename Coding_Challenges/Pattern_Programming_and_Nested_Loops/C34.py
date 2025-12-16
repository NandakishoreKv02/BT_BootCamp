def print_star_pattern(n):
    """
    Prints a star pattern with n rows and 5 stars per row.

    Args:
        n (int): Number of rows

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    for _ in range(n):
        for _ in range(5):
            print("*", end="")
        print()  # Move to next line


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    print_star_pattern(n)
