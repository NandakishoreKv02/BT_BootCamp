import unittest
from starter_code import Notifier, EmailNotifier, SMSNotifier, PagerNotifier

class TestPolymorphicNotification(unittest.TestCase):
    def test_all_inherit_from_notifier(self):
        self.assertTrue(issubclass(EmailNotifier, Notifier))
        self.assertTrue(issubclass(SMSNotifier, Notifier))
        self.assertTrue(issubclass(PagerNotifier, Notifier))
        
    def test_email_formatting(self):
        e = EmailNotifier()
        self.assertIn("Email to", e.send_alert("Test", "user@test.com"))
        
    def test_sms_formatting(self):
        s = SMSNotifier()
        self.assertIn("SMS to", s.send_alert("Test", "+1"))

if __name__ == "__main__":
    unittest.main()
