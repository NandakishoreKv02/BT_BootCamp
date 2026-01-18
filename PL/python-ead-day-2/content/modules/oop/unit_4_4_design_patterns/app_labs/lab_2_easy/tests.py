import unittest
from starter_code import ReportFactory, PDFReport, CSVReport, MedicalReport

class TestLab2(unittest.TestCase):
    def test_pdf_creation(self):
        report = ReportFactory.get_report("pdf")
        self.assertIsInstance(report, PDFReport)
        self.assertIn("[PDF]", report.generate("test"))

    def test_csv_creation(self):
        report = ReportFactory.get_report("csv")
        self.assertIsInstance(report, CSVReport)
        self.assertIn("[CSV]", report.generate("test"))

    def test_order_independence(self):
        r1 = ReportFactory.get_report("CSV") # Case insensitive test
        self.assertIsInstance(r1, CSVReport)

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            ReportFactory.get_report("html")

if __name__ == '__main__':
    unittest.main()
