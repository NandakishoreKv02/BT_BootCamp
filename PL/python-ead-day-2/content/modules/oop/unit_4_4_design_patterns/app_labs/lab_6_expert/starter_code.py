from abc import ABC, abstractmethod

class SystemConfig:
    _instance = None

    def __new__(cls):
        # TODO: Implement logic
        pass

class RiskStrategy(ABC):

    @abstractmethod
    def evaluate(self, val):
        # TODO: Implement logic
        pass

class AdultStrategy(RiskStrategy):

    def evaluate(self, val):
        # TODO: Implement logic
        pass

class PediatricStrategy(RiskStrategy):

    def evaluate(self, val):
        # TODO: Implement logic
        pass

class Subject:

    def __init__(self):
        # TODO: Implement logic
        pass

    def attach(self, o):
        # TODO: Implement logic
        pass

    def notify(self, m):
        # TODO: Implement logic
        pass

class Observer(ABC):

    @abstractmethod
    def update(self, m):
        # TODO: Implement logic
        pass

class Report(ABC):

    @abstractmethod
    def print(self, data):
        # TODO: Implement logic
        pass

class PDFReport(Report):

    def print(self, data):
        # TODO: Implement logic
        pass

class ReportFactory:

    @staticmethod
    def get(fmt):
        # TODO: Implement logic
        pass

class MedGuardSystem(Subject):
    """
    TODO: Integrate all patterns.
    """

    def __init__(self):
        # TODO: Implement logic
        pass

    def enroll_patient(self, name, type_char):
        # TODO: Implement logic
        pass

    def process_telemetry(self, name, hr):
        # TODO: Implement logic
        pass

    def close_and_report(self, name, fmt):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    # TODO: Implement logic
    pass