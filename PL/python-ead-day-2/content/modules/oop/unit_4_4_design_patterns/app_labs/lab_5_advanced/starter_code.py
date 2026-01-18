from abc import ABC, abstractmethod

class TreatmentStrategy(ABC):

    @abstractmethod
    def execute(self) -> str:
        # TODO: Implement logic
        pass

class ProtocolFactory:

    @staticmethod
    def get_protocol(condition: str) -> TreatmentStrategy:
        # TODO: Implement logic
        pass

class PatientManager:

    def __init__(self, name: str):
        # TODO: Implement logic
        pass

    def assign_protocol(self, condition: str):
        # TODO: Implement logic
        pass

    def run_treatment(self):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    # TODO: Implement logic
    pass