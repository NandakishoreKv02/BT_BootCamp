def find_largest(a, b, c):
    """
    Finds the largest of three numbers.

    Args:
        a (int or float): First number
        b (int or float): Second number
        c (int or float): Third number

    Returns:
        int or float: Largest number
    """
    return max(a, b, c)


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    largest = find_largest(num1, num2, num3)
    print("The largest number is:", largest)
