def search_element(arr, key):
    """
    Searches for a key element in the array.

    Args:
        arr (list): List of integers
        key (int): Element to search

    Returns:
        int: Index if found, otherwise -1

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    for index in range(len(arr)):
        if arr[index] == key:
            return index

    return -1


if __name__ == "__main__":
    try:
        n = int(input("Size: "))
        arr = [int(input()) for _ in range(n)]
        key = int(input("Enter element to search: "))
        result = search_element(arr, key)

        if result != -1:
            print(f"Element found at index {result}")
        else:
            print("Element not found")
    except ValueError as e:
        print("Error:", e)
