"""
Starter Code - Reset
"""
'Lab 2: Solution - Patient Registry'

class Patient:

    def __init__(self, patient_id, name):
        # TODO: Implement logic
        pass

    def __repr__(self):
        # TODO: Implement logic
        pass

class PatientRegistry:

    def __init__(self):
        # TODO: Implement logic
        pass

    def register(self, patient):
        # TODO: Implement logic
        pass

    def __len__(self):
        # TODO: Implement logic
        pass

    def __getitem__(self, patient_id):
        # TODO: Implement logic
        pass

    def __contains__(self, patient_id):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    registry = PatientRegistry()
    registry.register(Patient('P001', 'Alice'))
    registry.register(Patient('P002', 'Bob'))
    print(len(registry))
    print(registry['P001'])
    print('P001' in registry)