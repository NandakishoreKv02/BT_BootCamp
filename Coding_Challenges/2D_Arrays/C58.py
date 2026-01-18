def transpose_matrix(matrix):
    """
    Computes the transpose of a matrix.

    Args:
        matrix (list): 2D list of integers

    Returns:
        list: Transposed matrix

    Raises:
        ValueError: If matrix is empty or irregular
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")

    rows = len(matrix)
    cols = len(matrix[0])

    for row in matrix:
        if len(row) != cols:
            raise ValueError("Irregular matrix not allowed")

    transpose = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)

    return transpose


if __name__ == "__main__":
    try:
        r = int(input("Rows: "))
        c = int(input("Columns: "))
        mat = []
        print("Enter matrix:")
        for i in range(r):
            mat.append([int(input()) for _ in range(c)])

        print("Original Matrix:")
        for row in mat:
            print(*row)

        print("Transpose:")
        for row in transpose_matrix(mat):
            print(*row)
    except ValueError as e:
        print("Error:", e)
