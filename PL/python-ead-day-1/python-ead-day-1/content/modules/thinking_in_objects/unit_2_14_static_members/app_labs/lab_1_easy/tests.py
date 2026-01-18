import unittest
import starter_code

class TestStaticCounter(unittest.TestCase):
    def test_increment(self):
        # Reset counter if possible (depends on implementation)
        # Note: In a real lab, the counter might persist. 
        # We check relative increase.
        initial = starter_code.BedAdmission.occupied_beds
        starter_code.BedAdmission("Test 1")
        starter_code.BedAdmission("Test 2")
        self.assertEqual(starter_code.BedAdmission.occupied_beds, initial + 2)

if __name__ == "__main__":
    unittest.main()
