def display_fibonacci(n):
    """
    Displays the Fibonacci series up to n terms.

    Args:
        n (int): Number of terms in the series

    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("N must be a positive integer")

    a, b = 1, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    n = int(input("Enter number of terms (N): "))
    display_fibonacci(n)
