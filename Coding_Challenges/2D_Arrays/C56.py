def sum_of_matrix(matrix):
    """
    Computes the sum of all elements in a 2D matrix.

    Args:
        matrix (list): 2D list of integers

    Returns:
        int: Sum of elements

    Raises:
        ValueError: If matrix is empty or invalid
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")

    total = 0
    for row in matrix:
        for value in row:
            if not isinstance(value, int):
                raise ValueError("Matrix must contain only integers")
            total += value
    return total


if __name__ == "__main__":
    try:
        r = int(input("Rows: "))
        c = int(input("Columns: "))
        mat = []
        print("Enter matrix elements:")
        for i in range(r):
            mat.append([int(input()) for _ in range(c)])
        print("Sum =", sum_of_matrix(mat))
    except ValueError as e:
        print("Error:", e)
