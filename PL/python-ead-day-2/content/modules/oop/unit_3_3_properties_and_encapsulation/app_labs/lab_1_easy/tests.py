"""
Lab 1: Patient Vital Signs Monitor - Basic Properties
Test Suite
"""

import unittest
from starter_code import VitalSigns


class TestVitalSignsBasicProperties(unittest.TestCase):
    """Test cases for VitalSigns class with basic properties."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.vitals = VitalSigns("P12345", 37.2, 72, 120, 80)
    
    def test_patient_id_property(self):
        """Test patient_id property returns correct value."""
        self.assertEqual(self.vitals.patient_id, "P12345")
    
    def test_temperature_property(self):
        """Test temperature property returns correct value."""
        self.assertEqual(self.vitals.temperature, 37.2)
        self.assertIsInstance(self.vitals.temperature, float)
    
    def test_heart_rate_property(self):
        """Test heart_rate property returns correct value."""
        self.assertEqual(self.vitals.heart_rate, 72)
        self.assertIsInstance(self.vitals.heart_rate, int)
    
    def test_blood_pressure_property(self):
        """Test blood_pressure property returns formatted string."""
        self.assertEqual(self.vitals.blood_pressure, "120/80")
        self.assertIsInstance(self.vitals.blood_pressure, str)
    
    def test_properties_are_read_only(self):
        """Test that properties cannot be set directly."""
        with self.assertRaises(AttributeError):
            self.vitals.temperature = 38.0
        
        with self.assertRaises(AttributeError):
            self.vitals.heart_rate = 80
        
        with self.assertRaises(AttributeError):
            self.vitals.patient_id = "P99999"
    
    def test_private_attributes_exist(self):
        """Test that private attributes are created."""
        self.assertTrue(hasattr(self.vitals, '_patient_id'))
        self.assertTrue(hasattr(self.vitals, '_temperature'))
        self.assertTrue(hasattr(self.vitals, '_heart_rate'))
        self.assertTrue(hasattr(self.vitals, '_bp_systolic'))
        self.assertTrue(hasattr(self.vitals, '_bp_diastolic'))
    
    def test_str_representation(self):
        """Test string representation of VitalSigns."""
        expected = "Patient P12345: Temp=37.2C, HR=72bpm, BP=120/80"
        self.assertEqual(str(self.vitals), expected)
    
    def test_different_values(self):
        """Test with different vital signs values."""
        vitals2 = VitalSigns("P99999", 38.5, 95, 140, 90)
        self.assertEqual(vitals2.patient_id, "P99999")
        self.assertEqual(vitals2.temperature, 38.5)
        self.assertEqual(vitals2.heart_rate, 95)
        self.assertEqual(vitals2.blood_pressure, "140/90")


if __name__ == "__main__":
    unittest.main()
