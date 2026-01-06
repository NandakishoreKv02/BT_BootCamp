def search_element(matrix, target):
    """
    Checks whether a target element exists in a 2D matrix.

    Args:
        matrix (list): 2D list of integers
        target (int): Element to search

    Returns:
        bool: True if found, False otherwise

    Raises:
        ValueError: If matrix is invalid
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")

    for row in matrix:
        for value in row:
            if value == target:
                return True
    return False


if __name__ == "__main__":
    try:
        r = int(input("Rows: "))
        c = int(input("Columns: "))
        mat = []
        print("Enter matrix elements:")
        for i in range(r):
            mat.append([int(input()) for _ in range(c)])
        key = int(input("Enter element to search: "))
        print("Element found" if search_element(mat, key) else "Element not found")
    except ValueError as e:
        print("Error:", e)
