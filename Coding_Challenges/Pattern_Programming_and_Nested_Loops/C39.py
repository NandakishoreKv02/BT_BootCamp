def print_alternating_square_pattern(n):
    """
    Prints a pattern of perfect squares with alternating signs in n rows.
    Each row contains 6 numbers.

    Args:
        n (int): Number of rows

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    num = 1  # Base number to square
    position = True  # Tracks sign alternation

    for i in range(n+1):
        for _ in range(i):
            square = num * num
            if not position:
                print(f"-{square}", end=" ")
                position = True
            else:
                print(square, end=" ")
                position = False
            num += 1
        print()  # New line after each row


if __name__ == "__main__":
    n = int(input("Enter number of rows (N): "))
    print_alternating_square_pattern(n)
