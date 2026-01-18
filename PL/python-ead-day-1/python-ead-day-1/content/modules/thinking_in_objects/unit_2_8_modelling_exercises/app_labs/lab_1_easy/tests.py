import unittest
import starter_code

class TestInventoryModelling(unittest.TestCase):
    def test_composition(self):
        inv = starter_code.Inventory()
        inv.add_stock("Guaze", 10)
        
        self.assertEqual(len(inv.items), 1)
        self.assertEqual(inv.items[0].name, "Guaze")
        self.assertTrue(isinstance(inv.items[0], starter_code.SupplyItem))

if __name__ == "__main__":
    unittest.main()
