"""
Unit 4.4: Design Patterns - Exercises
Master Singleton, Factory, Observer, and Strategy patterns.
"""

from abc import ABC, abstractmethod

# ============================================================================
# Exercise 1: App Settings Singleton
# ============================================================================

class AppSettings:
    """
    TODO: Implement the Singleton pattern.
    Only one instance of AppSettings should ever exist.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # We only want to initialize once
        if not hasattr(self, 'settings'):
            self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)


# ============================================================================
# Exercise 2: Notification Factory
# ============================================================================

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        return f"Sending Email: {message}"

class SMSNotification(Notification):
    def send(self, message: str):
        return f"Sending SMS: {message}"

class NotificationFactory:
    """
    TODO: Implement the Factory pattern.
    Should return a Notification object based on the type string.
    """
    @staticmethod
    def create_notification(noti_type: str) -> Notification:
        if noti_type == "email":
            return EmailNotification()
        elif noti_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("Invalid notification type")


# ============================================================================
# Exercise 3: Emergency Alert Observer
# ============================================================================

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

class VitalMonitor(Subject):
    """
    TODO: Implement a monitor that triggers an alert.
    """
    def check_vitals(self, heart_rate: int):
        if heart_rate > 120 or heart_rate < 50:
            self.notify(f"Critical heart rate: {heart_rate}")

class NurseStation(Observer):
    def update(self, message: str):
        return f"Nurse Station received: {message}"


# ============================================================================
# Exercise 4: Compression Strategy
# ============================================================================

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data: str) -> str:
        pass

class ZipStrategy(CompressionStrategy):
    def compress(self, data: str) -> str:
        return f"ZIP: {data}"

class TarStrategy(CompressionStrategy):
    def compress(self, data: str) -> str:
        return f"TAR: {data}"

class FileArchiver:
    """
    TODO: Implement the Strategy pattern.
    Allow switching compression strategies at runtime.
    """
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy):
        self.strategy = strategy

    def archive(self, data: str) -> str:
        return self.strategy.compress(data)


# ============================================================================
# Test Cases
# ============================================================================

if __name__ == "__main__":
    print("Running Design Pattern Exercises...")
    
    # Ex 1: Singleton
    s1 = AppSettings()
    s2 = AppSettings()
    print(f"Ex 1: Singleton identical: {s1 is s2}")

    # Ex 2: Factory
    try:
        email = NotificationFactory.create_notification("email")
        print(f"Ex 2: {email.send('Hello')}")
    except:
        print("Ex 2: Not implemented")

    # Ex 3: Observer
    monitor = VitalMonitor()
    nurse = NurseStation()
    monitor.attach(nurse)
    # monitor.check_vitals(150) # Should trigger notify

    # Ex 4: Strategy
    archiver = FileArchiver(ZipStrategy())
    # print(f"Ex 4: {archiver.archive('report.pdf')}")
    # archiver.set_strategy(TarStrategy())
    # print(f"Ex 4: {archiver.archive('report.pdf')}")
