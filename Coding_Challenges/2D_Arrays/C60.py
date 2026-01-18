def multiply_matrices(A, B):
    """
    Multiplies two matrices.

    Args:
        A (list): First matrix
        B (list): Second matrix

    Returns:
        list: Resultant matrix

    Raises:
        ValueError: If multiplication is not possible
    """
    if not A or not B:
        raise ValueError("Matrices cannot be empty")

    if len(A[0]) != len(B):
        raise ValueError("Matrix multiplication not possible")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


if __name__ == "__main__":
    try:
        r1 = int(input("Rows of A: "))
        c1 = int(input("Columns of A: "))
        r2 = int(input("Rows of B: "))
        c2 = int(input("Columns of B: "))

        A = [[int(input()) for _ in range(c1)] for _ in range(r1)]
        B = [[int(input()) for _ in range(c2)] for _ in range(r2)]

        result = multiply_matrices(A, B)

        print("Result Matrix:")
        for row in result:
            print(*row)

    except ValueError as e:
        print("Error:", e)
