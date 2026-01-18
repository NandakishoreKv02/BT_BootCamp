def display_series(n):
    """
    Displays the series: 1, 2, 4, 7, 11, 16, 22 ... up to n terms.

    Args:
        n (int): Number of terms in the series

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("N must be a positive integer")

    current = 1
    diff = 1

    for _ in range(n):
        print(current, end=" ")
        current += diff
        diff += 1


if __name__ == "__main__":
    n = int(input("Enter number of terms (N): "))
    display_series(n)
