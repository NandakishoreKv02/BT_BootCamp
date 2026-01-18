def get_shared_patients(er_set, icu_set):
    return er_set & icu_set

def get_all_unique_patients(er_set, icu_set):
    return er_set | icu_set

def get_er_only_patients(er_set, icu_set):
    return er_set - icu_set

def get_single_dept_visitors(er_set, icu_set):
    return er_set ^ icu_set
