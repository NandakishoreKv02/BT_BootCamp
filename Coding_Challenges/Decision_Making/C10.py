def get_student_class(average):
    """
    Determines the class secured based on average marks.

    Args:
        average (float): Average score

    Returns:
        str: Class secured
    """
    if average >= 60:
        return "1st Class"
    elif average >= 50:
        return "2nd Class"
    elif average >= 35:
        return "Pass Class"
    else:
        return "Fail"


if __name__ == "__main__":
    name = input("Enter student name: ")

    marks1 = float(input("Enter marks for Subject 1: "))
    marks2 = float(input("Enter marks for Subject 2: "))
    marks3 = float(input("Enter marks for Subject 3: "))

    for marks in (marks1, marks2, marks3):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

    total = marks1 + marks2 + marks3
    average = total / 3

    student_class = get_student_class(average)

    print("\n--- Student Report Card ---")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Class Secured:", student_class)
