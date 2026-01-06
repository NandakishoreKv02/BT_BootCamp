def sort_array(arr, order):
    """
    Sorts the array in ascending or descending order.

    Args:
        arr (list): List of integers
        order (str): 'asc' for ascending, 'desc' for descending

    Returns:
        list: Sorted array

    Raises:
        ValueError: If input order is invalid
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    sorted_arr = arr.copy()

    for i in range(len(sorted_arr)):
        for j in range(i + 1, len(sorted_arr)):
            if (order == "asc" and sorted_arr[i] > sorted_arr[j]) or \
               (order == "desc" and sorted_arr[i] < sorted_arr[j]):
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]

    return sorted_arr


if __name__ == "__main__":
    try:
        n = int(input("Enter array size: "))
        arr = [int(input()) for _ in range(n)]
        choice = input("Enter order (asc/desc): ").lower()

        if choice not in ("asc", "desc"):
            raise ValueError("Invalid sorting order")

        print("Sorted Array:", sort_array(arr, choice))
    except ValueError as e:
        print("Error:", e)
