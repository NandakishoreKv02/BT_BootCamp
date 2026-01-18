class Patient:

    def __init__(self, name, age, condition):
        # TODO: Implement logic
        pass

    @classmethod
    def from_string(cls, data_str):
        # TODO: Implement logic
        pass

    @classmethod
    def from_dict(cls, data_dict):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    p1 = Patient.from_string('Alice:30:Flu')
    print(f'Name: {p1.name}, Age: {p1.age}')