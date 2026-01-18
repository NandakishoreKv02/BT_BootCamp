def binary_search(arr, key):
    """
    Performs binary search on a sorted array.

    Args:
        arr (list): Sorted list of integers
        key (int): Element to search

    Returns:
        int: Index of element if found, otherwise -1

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    try:
        n = int(input("Enter array size: "))
        arr = [int(input()) for _ in range(n)]
        arr.sort()  # Ensuring sorted array for binary search

        search_key = int(input("Enter element to search: "))
        index = binary_search(arr, search_key)

        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found")
    except ValueError as e:
        print("Error:", e)
