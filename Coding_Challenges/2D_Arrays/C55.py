def create_and_display_matrix(rows, cols, elements):
    """
    Creates a 2D matrix and displays its elements row-wise.

    Args:
        rows (int): Number of rows
        cols (int): Number of columns
        elements (list): Flat list of matrix elements

    Returns:
        list: 2D matrix

    Raises:
        ValueError: If rows or cols are non-positive or element count mismatches
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive integers")

    if len(elements) != rows * cols:
        raise ValueError("Number of elements does not match matrix size")

    matrix = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[index])
            index += 1
        matrix.append(row)

    for row in matrix:
        print(*row)

    return matrix


if __name__ == "__main__":
    try:
        r = int(input("Enter rows: "))
        c = int(input("Enter columns: "))
        elems = []
        print("Enter elements:")
        for _ in range(r * c):
            elems.append(int(input()))
        create_and_display_matrix(r, c, elems)
    except ValueError as e:
        print("Error:", e)
