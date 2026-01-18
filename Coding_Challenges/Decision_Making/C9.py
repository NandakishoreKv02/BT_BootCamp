def is_leap_year(year):
    """
    Checks whether a given year is a leap year.

    Args:
        year (int): Year to check

    Returns:
        bool: True if leap year, False otherwise

    Raises:
        ValueError: If year is not a positive integer
    """
    if year <= 0:
        raise ValueError("Year must be a positive integer")

    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
