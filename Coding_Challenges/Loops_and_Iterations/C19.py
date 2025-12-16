def display_even_square_series(n):
    """
    Displays the series: 4, 16, 36, 64 ... for n terms.

    Args:
        n (int): Number of terms in the series

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("N must be a positive integer")

    even_number = 2
    for _ in range(n):
        print(even_number ** 2, end=" ")
        even_number += 2


if __name__ == "__main__":
    n = int(input("Enter number of terms (N): "))
    display_even_square_series(n)
