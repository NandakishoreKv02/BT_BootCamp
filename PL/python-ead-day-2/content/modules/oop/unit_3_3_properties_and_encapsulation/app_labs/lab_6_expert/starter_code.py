"""
Starter Code - Reset
"""
'Lab 6: Solution'

class CapacityError(Exception):
    # TODO: Implement logic
    pass

class Patient:

    def __init__(self, patient_id, name):
        # TODO: Implement logic
        pass

class CriticalCareUnit:

    def __init__(self, name, max_capacity):
        # TODO: Implement logic
        pass

    def _log(self, message):
        # TODO: Implement logic
        pass

    @property
    def max_capacity(self):
        # TODO: Implement logic
        pass

    @max_capacity.setter
    def max_capacity(self, value):
        # TODO: Implement logic
        pass

    @property
    def audit_log(self):
        # TODO: Implement logic
        pass

    def admit_patient(self, patient):
        # TODO: Implement logic
        pass

    def discharge_patient(self, patient_id):
        # TODO: Implement logic
        pass

    @property
    def occupancy_rate(self):
        # TODO: Implement logic
        pass

    @property
    def patient_ids(self):
        # TODO: Implement logic
        pass

    @property
    def is_full(self):
        # TODO: Implement logic
        pass

    def get_patient(self, patient_id):
        # TODO: Implement logic
        pass