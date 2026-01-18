from abc import ABC, abstractmethod

class AlertStrategy(ABC):

    @abstractmethod
    def evaluate(self, data: list) -> bool:
        # TODO: Implement logic
        pass

class ThresholdStrategy(AlertStrategy):
    # TODO: Implement logic
    pass

class AverageStrategy(AlertStrategy):
    # TODO: Implement logic
    pass

class PatientMonitor:

    def __init__(self, patient_name: str, strategy: AlertStrategy):
        # TODO: Implement logic
        pass

    def add_data(self, value: float):
        # TODO: Implement logic
        pass

    def check_status(self) -> bool:
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    data = [98, 99, 105, 99]
    # TODO: Implement logic
    pass