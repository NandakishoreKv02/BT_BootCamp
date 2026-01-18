import unittest
import json
import os
from starter_code import load_config, DEFAULT_CONFIG

class TestLab6(unittest.TestCase):
    def test_missing_file(self):
        cfg = load_config("missing_file_123.json")
        self.assertEqual(cfg, DEFAULT_CONFIG)

    def test_corrupted_file(self):
        with open("bad.json", "w") as f:
            f.write("{broken_json")
        try:
            cfg = load_config("bad.json")
            self.assertEqual(cfg, DEFAULT_CONFIG)
        finally:
            os.remove("bad.json")

    def test_valid_file(self):
        valid = {"mode": "pro", "retries": 5}
        with open("good.json", "w") as f:
            json.dump(valid, f)
        try:
            cfg = load_config("good.json")
            self.assertEqual(cfg, valid)
        finally:
            os.remove("good.json")

if __name__ == "__main__":
    unittest.main()
