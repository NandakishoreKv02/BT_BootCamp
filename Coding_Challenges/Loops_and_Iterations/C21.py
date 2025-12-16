def display_square_series(n):
    """
    Displays the series of square numbers up to n terms.

    Args:
        n (int): Number of terms in the series

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("N must be a positive integer")

    for i in range(1, n + 1):
        print(i * i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter number of terms (N): "))
    display_square_series(n)
