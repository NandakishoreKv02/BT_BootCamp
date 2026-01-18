import unittest
from starter_code import MedicalDevice

class TestAbstraction(unittest.TestCase):
    def test_cannot_instantiate_abc(self):
        with self.assertRaises(TypeError):
            MedicalDevice()

if __name__ == "__main__":
    unittest.main()
