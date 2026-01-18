"""
Starter Code - Reset
"""
'Lab 5: Solution - Validation Engine'
import re

class RangeValidator:

    def __init__(self, min_value: float, max_value: float, field_name: str='value'):
        # TODO: Implement logic
        pass

    def __call__(self, value):
        # TODO: Implement logic
        pass

    def __repr__(self):
        # TODO: Implement logic
        pass

class PatternValidator:

    def __init__(self, pattern: str, field_name: str='value'):
        # TODO: Implement logic
        pass

    def __call__(self, value):
        # TODO: Implement logic
        pass

class ValidatorChain:

    def __init__(self, validators: list=None):
        # TODO: Implement logic
        pass

    def add(self, validator):
        # TODO: Implement logic
        pass

    def __call__(self, value):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    temp_validator = RangeValidator(35.0, 42.0, 'temperature')
    print(temp_validator(37.5))
    try:
        temp_validator(45.0)
    except ValueError as e:
        print(f'Validation failed: {e}')