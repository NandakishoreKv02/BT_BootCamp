def calculate_dose_per_intake(total_mg, frequency):
    """
    TODO:
    1. Try to divide total_mg / frequency.
    2. Catch ZeroDivisionError -> print error, return None.
    3. Catch (TypeError, ValueError) -> print error, return None.
    4. Else -> return rounded result (2 decimal places).
    """
    # WRITE CODE HERE
    pass

def main():
    print(calculate_dose_per_intake(500, 3))    # 166.67
    print(calculate_dose_per_intake(500, 0))    # None
    print(calculate_dose_per_intake("500", 2))  # Error (strings don't divide)

if __name__ == "__main__":
    main()
