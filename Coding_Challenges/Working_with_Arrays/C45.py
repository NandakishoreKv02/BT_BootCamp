def create_array(n, elements):
    """
    Creates an array of size n.

    Args:
        n (int): Size of the array
        elements (list): List of integers

    Returns:
        list: Array containing n elements

    Raises:
        ValueError: If n is invalid or elements count mismatches
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Array size must be a positive integer")

    if len(elements) != n:
        raise ValueError("Number of elements must be equal to n")

    for value in elements:
        if not isinstance(value, int):
            raise ValueError("Array must contain only integers")

    return elements


if __name__ == "__main__":
    try:
        n = int(input("Enter array size: "))
        print("Enter elements:")
        arr = [int(input()) for _ in range(n)]
        array = create_array(n, arr)
        print("Array:", array)
    except ValueError as e:
        print("Error:", e)
