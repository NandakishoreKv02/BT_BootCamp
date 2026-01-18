import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestMedicationInventory(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.inventory = []

    def test_create_medication(self):
        med = starter_code.create_medication("Aspirin", 100, 50)
        self.assertEqual(med["name"], "Aspirin")
        self.assertEqual(med["quantity"], 100)
        self.assertEqual(med["reorder_level"], 50)

    def test_add_to_inventory(self):
        med = starter_code.create_medication("Test", 10, 5)
        starter_code.add_to_inventory(self.inventory, med)
        self.assertEqual(len(self.inventory), 1)

    def test_find_medication(self):
        med1 = starter_code.create_medication("Aspirin", 100, 50)
        med2 = starter_code.create_medication("Ibuprofen", 75, 30)
        starter_code.add_to_inventory(self.inventory, med1)
        starter_code.add_to_inventory(self.inventory, med2)
        
        idx = starter_code.find_medication(self.inventory, "Ibuprofen")
        self.assertEqual(idx, 1)
        
        idx_not_found = starter_code.find_medication(self.inventory, "NotExist")
        self.assertEqual(idx_not_found, -1)

    def test_update_stock(self):
        med = starter_code.create_medication("Aspirin", 100, 50)
        starter_code.add_to_inventory(self.inventory, med)
        
        result = starter_code.update_stock(self.inventory, "Aspirin", -20)
        self.assertTrue(result)
        self.assertEqual(self.inventory[0]["quantity"], 80)

    def test_get_low_stock(self):
        med1 = starter_code.create_medication("Aspirin", 100, 50)
        med2 = starter_code.create_medication("Ibuprofen", 25, 30)
        starter_code.add_to_inventory(self.inventory, med1)
        starter_code.add_to_inventory(self.inventory, med2)
        
        low_stock = starter_code.get_low_stock_items(self.inventory)
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0]["name"], "Ibuprofen")

if __name__ == '__main__':
    unittest.main()
