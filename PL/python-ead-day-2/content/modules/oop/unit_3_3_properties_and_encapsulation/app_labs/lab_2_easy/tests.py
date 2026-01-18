"""
Lab 2: Patient Vital Signs Monitor - Setters & Validation
Test Suite
"""

import unittest
from starter_code import VitalSigns


class TestVitalSignsValidation(unittest.TestCase):
    """Test cases for VitalSigns validation."""
    
    def test_valid_temperature_update(self):
        """Test valid temperature update."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        vitals.temperature = 38.5
        self.assertEqual(vitals.temperature, 38.5)
    
    def test_invalid_temperature_low(self):
        """Test temperature below minimum raises ValueError."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        with self.assertRaises(ValueError):
            vitals.temperature = 34.0
    
    def test_invalid_temperature_high(self):
        """Test temperature above maximum raises ValueError."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        with self.assertRaises(ValueError):
            vitals.temperature = 43.0
    
    def test_valid_heart_rate_update(self):
        """Test valid heart rate update."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        vitals.heart_rate = 85
        self.assertEqual(vitals.heart_rate, 85)
    
    def test_invalid_heart_rate_low(self):
        """Test heart rate below minimum raises ValueError."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        with self.assertRaises(ValueError):
            vitals.heart_rate = 30
    
    def test_invalid_heart_rate_high(self):
        """Test heart rate above maximum raises ValueError."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        with self.assertRaises(ValueError):
            vitals.heart_rate = 250
    
    def test_set_blood_pressure_valid(self):
        """Test setting valid blood pressure."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        vitals.set_blood_pressure(130, 85)
        self.assertEqual(vitals.bp_systolic, 130)
        self.assertEqual(vitals.bp_diastolic, 85)
    
    def test_set_blood_pressure_invalid_systolic_greater(self):
        """Test systolic must be greater than diastolic."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        with self.assertRaises(ValueError):
            vitals.set_blood_pressure(80, 90)
    
    def test_update_vitals_all_valid(self):
        """Test updating all vitals with valid values."""
        vitals = VitalSigns("P001", 37.0, 70, 120, 80)
        vitals.update_vitals(38.0, 85, 130, 85)
        self.assertEqual(vitals.temperature, 38.0)
        self.assertEqual(vitals.heart_rate, 85)
        self.assertEqual(vitals.blood_pressure, "130/85")


if __name__ == "__main__":
    unittest.main()
