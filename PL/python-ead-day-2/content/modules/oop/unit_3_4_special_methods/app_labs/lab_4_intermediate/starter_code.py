"""
Starter Code - Reset
"""
'Lab 4: Solution - Diagnosis Codes'

class DiagnosisCode:

    def __init__(self, code: str, description: str):
        # TODO: Implement logic
        pass

    def __eq__(self, other):
        # TODO: Implement logic
        pass

    def __hash__(self):
        # TODO: Implement logic
        pass

    def __repr__(self):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    d1 = DiagnosisCode('J06.9', 'Acute upper respiratory infection')
    d2 = DiagnosisCode('J06.9', 'URI')
    print(d1 == d2)
    print(len({d1, d2}))