def sum_of_array(arr):
    """
    Computes the sum of all elements in the array.

    Args:
        arr (list): List of integers

    Returns:
        int: Sum of elements

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    total = 0
    for value in arr:
        total += value

    return total


if __name__ == "__main__":
    try:
        n = int(input("Size: "))
        arr = [int(input()) for _ in range(n)]
        print("Sum =", sum_of_array(arr))
    except ValueError as e:
        print("Error:", e)
