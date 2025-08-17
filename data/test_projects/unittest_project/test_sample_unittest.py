import unittest
import os
import sys

# Add the current directory to the path so Python can find the module
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from sample_module import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    # def test_add_redundant(self):
    #     self.assertEqual(add(2, 3), 5)  # Redundant
    #     self.assertEqual(add(0, 0), 0)  # Redundant

if __name__ == "__main__":
    unittest.main()
