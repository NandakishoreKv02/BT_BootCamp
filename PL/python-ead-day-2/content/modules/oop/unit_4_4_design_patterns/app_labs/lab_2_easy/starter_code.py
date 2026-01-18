from abc import ABC, abstractmethod

class MedicalReport(ABC):

    @abstractmethod
    def generate(self, data: str) -> str:
        # TODO: Implement logic
        pass

class PDFReport:
    # TODO: Implement logic
    pass

class CSVReport:
    # TODO: Implement logic
    pass

class ReportFactory:

    @staticmethod
    def get_report(format_type: str) -> MedicalReport:
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    # TODO: Implement logic
    pass