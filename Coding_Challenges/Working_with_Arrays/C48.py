def find_maximum(arr):
    """
    Finds the maximum value in the array.

    Args:
        arr (list): List of integers

    Returns:
        int: Maximum element

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    maximum = arr[0]
    for value in arr:
        if value > maximum:
            maximum = value

    return maximum


if __name__ == "__main__":
    try:
        n = int(input("Size: "))
        arr = [int(input()) for _ in range(n)]
        print("Maximum =", find_maximum(arr))
    except ValueError as e:
        print("Error:", e)
