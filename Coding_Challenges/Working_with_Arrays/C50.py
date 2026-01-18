def count_even_odd(arr):
    """
    Counts the number of even and odd elements in the array.

    Args:
        arr (list): List of integers

    Returns:
        tuple: (even_count, odd_count)

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    even = 0
    odd = 0

    for value in arr:
        if value % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


if __name__ == "__main__":
    try:
        n = int(input("Size: "))
        arr = [int(input()) for _ in range(n)]
        even_count, odd_count = count_even_odd(arr)
        print("Even numbers:", even_count)
        print("Odd numbers:", odd_count)
    except ValueError as e:
        print("Error:", e)
