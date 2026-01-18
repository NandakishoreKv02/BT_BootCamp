import unittest
from starter_code import ProtocolFactory, CardiacProtocol, TraumaProtocol, DefaultProtocol, PatientManager

class TestLab5(unittest.TestCase):
    def test_factory_mapping(self):
        self.assertIsInstance(ProtocolFactory.get_protocol("cardiac"), CardiacProtocol)
        self.assertIsInstance(ProtocolFactory.get_protocol("trauma"), TraumaProtocol)
        self.assertIsInstance(ProtocolFactory.get_protocol("unknown"), DefaultProtocol)

    def test_manager_integration(self):
        pm = PatientManager("Test")
        pm.assign_protocol("cardiac")
        self.assertIsInstance(pm.active_protocol, CardiacProtocol)

if __name__ == '__main__':
    unittest.main()
