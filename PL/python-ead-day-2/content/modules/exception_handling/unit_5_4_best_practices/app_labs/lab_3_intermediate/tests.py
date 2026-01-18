import unittest
from starter_code import safe_api_call, MockHospitalLogger

class TestLab3(unittest.TestCase):
    def test_logging_triggered(self):
        logger = MockHospitalLogger()
        def fail(): raise ConnectionError("Fail")
        
        safe_api_call(fail, logger)
        self.assertEqual(len(logger.logs), 1)
        self.assertEqual(logger.tracebacks_captured, 1)
        self.assertIn("API Error occurred", logger.logs[0])

    def test_success_no_log(self):
        logger = MockHospitalLogger()
        safe_api_call(lambda: "ok", logger)
        self.assertEqual(len(logger.logs), 0)

if __name__ == "__main__":
    unittest.main()
