import unittest
import starter_code

class TestSecurity(unittest.TestCase):
    def test_login_flow(self):
        logger = starter_code.AuditLog()
        acct = starter_code.PatientAccount("u", "p")
        
        self.assertTrue(acct.login("p", logger))
        self.assertFalse(acct.login("wrong", logger))
        
    def test_encapsulation(self):
        acct = starter_code.PatientAccount("u", "p")
        # Check standard convention for private attribute
        self.assertTrue(hasattr(acct, '_password') or hasattr(acct, '__password'))

if __name__ == "__main__":
    unittest.main()
