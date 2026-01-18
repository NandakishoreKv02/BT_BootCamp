from abc import ABC, abstractmethod

class RiskStrategy(ABC):

    @abstractmethod
    def evaluate(self, heart_rate: int) -> str:
        # TODO: Implement logic
        pass

class AdultStrategy(RiskStrategy):
    # TODO: Implement logic
    pass

class PediatricStrategy(RiskStrategy):
    # TODO: Implement logic
    pass

class PatientAssessor:

    def __init__(self, strategy: RiskStrategy):
        # TODO: Implement logic
        pass

    def set_strategy(self, strategy: RiskStrategy):
        # TODO: Implement logic
        pass

    def get_risk_level(self, hr: int) -> str:
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    # TODO: Implement logic
    pass