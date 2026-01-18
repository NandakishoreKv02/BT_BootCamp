# Lab 2 Tasks

## Task 1: Create the Base Interface
- Define an abstract class `MedicalReport`.
- Add an `@abstractmethod` called `generate(self, data)`.

## Task 2: Implement Concrete Reports
- Create `PDFReport` (Returns "[PDF]: {data}").
- Create `CSVReport` (Returns "[CSV]: {data}").

## Task 3: Implement the Factory
- Define class `ReportFactory`.
- Create a static method `get_report(format_type)`.
- If format is "pdf", return `PDFReport`.
- If format is "csv", return `CSVReport`.
- Otherwise, raise a `ValueError`.

## Task 4: Client Usage
- Use the factory to create a report.
- Print the result of calling `.generate()`.
