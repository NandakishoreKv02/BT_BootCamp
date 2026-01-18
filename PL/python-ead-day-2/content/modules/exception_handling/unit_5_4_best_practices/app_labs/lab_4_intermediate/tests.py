import unittest
from starter_code import secure_download_handler

class TestLab4(unittest.TestCase):
    def test_message_safety(self):
        logs = []
        msg = secure_download_handler("secret.pdf", logs)
        # Message should be polite and generic
        self.assertEqual(msg, "Unable to access report. Please try again later.")
        # Logs should contain the path
        self.assertIn("C:/MED_DATA/REPORTS/secret.pdf", logs[0])

if __name__ == "__main__":
    unittest.main()
