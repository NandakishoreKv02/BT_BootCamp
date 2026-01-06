def create_array(n, elements):
    """
    Creates an array of size n using provided elements.

    Args:
        n (int): Size of the array
        elements (list): List of integer elements

    Returns:
        list: Created array

    Raises:
        ValueError: If n is invalid or element count mismatches
    """
    if n <= 0:
        raise ValueError("Array size must be greater than zero")

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
        elems = [int(input()) for _ in range(n)]
        arr = create_array(n, elems)
        print("Array:", arr)
    except ValueError as e:
        print("Error:", e)
