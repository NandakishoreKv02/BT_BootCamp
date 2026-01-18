def display_matrix_and_transpose(matrix):
    """
    Displays a matrix and its transpose.

    Args:
        matrix (list): 2D integer matrix
    """
    print("Matrix:")
    for row in matrix:
        print(*row)

    print("Transpose:")
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    try:
        m = int(input("Rows: "))
        n = int(input("Columns: "))
        mat = []
        for i in range(m):
            mat.append([int(input()) for _ in range(n)])
        display_matrix_and_transpose(mat)
    except ValueError:
        print("Invalid input")
