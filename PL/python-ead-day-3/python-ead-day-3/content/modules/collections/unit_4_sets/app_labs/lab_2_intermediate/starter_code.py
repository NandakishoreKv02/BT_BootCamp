"""
Lab 2 (Intermediate): Cross-Department Analysis
Starter Code
"""

def get_shared_patients(er_set, icu_set):
    """
    Return patients present in both ER and ICU.
    """
    # TODO: Use & operator
    pass


def get_all_unique_patients(er_set, icu_set):
    """
    Return a combined set of all unique patients from both departments.
    """
    # TODO: Use | operator
    pass


def get_er_only_patients(er_set, icu_set):
    """
    Return patients in ER who were NEVER in ICU.
    """
    # TODO: Use - operator
    pass


def get_single_dept_visitors(er_set, icu_set):
    """
    Return patients who visited only one department (not both).
    """
    # TODO: Use ^ operator
    pass


if __name__ == "__main__":
    er = {101, 102, 105, 109}
    icu = {105, 110, 101, 120}
    
    print(f"ER: {er}, ICU: {icu}")
    print(f"Shared: {get_shared_patients(er, icu)}")
    print(f"All: {get_all_unique_patients(er, icu)}")
    print(f"ER Only: {get_er_only_patients(er, icu)}")
    print(f"Single Dept: {get_single_dept_visitors(er, icu)}")
