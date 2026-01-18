from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, message: str):
        # TODO: Implement logic
        pass

class Subject:

    def __init__(self):
        # TODO: Implement logic
        pass

    def attach(self, observer: Observer):
        # TODO: Implement logic
        pass

    def detach(self, observer: Observer):
        # TODO: Implement logic
        pass

    def notify(self, message: str):
        # TODO: Implement logic
        pass

class VitalMonitor(Subject):

    def check_heart_rate(self, hr: int):
        # TODO: Implement logic
        pass

class NurseStation(Observer):
    # TODO: Implement logic
    pass
if __name__ == '__main__':
    # TODO: Implement logic
    pass