def generate_series(n):
    """
    Generates the series: 1, -5, 9, -13, 17, -21 ... up to n terms.

    Args:
        n (int): Number of terms

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("N must be a positive integer")

    value = 1

    for i in range(1, n + 1):
        if i % 2 == 0:
            print(-value, end=" ")
        else:
            print(value, end=" ")
        value += 4


if __name__ == "__main__":
    n = int(input("Enter number of terms (N): "))
    generate_series(n)
