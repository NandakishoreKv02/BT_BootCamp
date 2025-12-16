def display_series(n):
    """
    Displays numbers from 1 to n.

    Args:
        n (int): Upper limit of the series

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("N must be a positive integer")

    for i in range(1, n + 1):
        print(i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter value of N: "))
    display_series(n)
