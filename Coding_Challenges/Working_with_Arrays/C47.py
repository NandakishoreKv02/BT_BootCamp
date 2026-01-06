def find_minimum(arr):
    """
    Finds the minimum value in the array.

    Args:
        arr (list): List of integers

    Returns:
        int: Minimum element

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    minimum = arr[0]
    for value in arr:
        if value < minimum:
            minimum = value

    return minimum


if __name__ == "__main__":
    try:
        n = int(input("Size: "))
        arr = [int(input()) for _ in range(n)]
        print("Minimum =", find_minimum(arr))
    except ValueError as e:
        print("Error:", e)
