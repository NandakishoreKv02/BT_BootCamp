def reverse_array(arr):
    """
    Reverses the given array.

    Args:
        arr (list): Input integer array

    Returns:
        list: Reversed array

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])

    return reversed_arr


if __name__ == "__main__":
    try:
        n = int(input("Enter array size: "))
        arr = [int(input()) for _ in range(n)]
        print("Reversed Array:", reverse_array(arr))
    except ValueError as e:
        print("Error:", e)
