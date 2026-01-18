"""
Starter Code - Reset
"""
'Lab 6: Solution - Complete Patient Manager'
from datetime import datetime
from functools import total_ordering

@total_ordering
class Patient:

    def __init__(self, patient_id, name, age):
        # TODO: Implement logic
        pass

    def __eq__(self, other):
        # TODO: Implement logic
        pass

    def __lt__(self, other):
        # TODO: Implement logic
        pass

    def __hash__(self):
        # TODO: Implement logic
        pass

    def __repr__(self):
        # TODO: Implement logic
        pass

class PatientManager:

    def __init__(self):
        # TODO: Implement logic
        pass

    def __len__(self):
        # TODO: Implement logic
        pass

    def __getitem__(self, patient_id):
        # TODO: Implement logic
        pass

    def __setitem__(self, patient_id, patient):
        # TODO: Implement logic
        pass

    def __delitem__(self, patient_id):
        # TODO: Implement logic
        pass

    def __contains__(self, patient_id):
        # TODO: Implement logic
        pass

    def __iter__(self):
        # TODO: Implement logic
        pass

    def __call__(self, **criteria):
        """Filter patients by criteria."""
        # TODO: Implement logic
        pass

    def __str__(self):
        # TODO: Implement logic
        pass

    def __repr__(self):
        # TODO: Implement logic
        pass

    def _log(self, action, details):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    manager = PatientManager()
    manager['P001'] = Patient('P001', 'Alice', 30)
    manager['P002'] = Patient('P002', 'Bob', 40)
    print(manager)
    print(list(manager))
    found = manager(name='Alice')
    print(f'Found: {len(found)}')