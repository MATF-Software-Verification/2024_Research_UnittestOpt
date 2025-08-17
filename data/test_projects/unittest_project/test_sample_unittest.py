import unittest
import os
import sys

# Add the current directory to the path so Python can find the module
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

class TestAbsDivisionFunction(unittest.TestCase):
    def test_all_positive_division(self):
        from sample_module import abs_divide
        assert abs_divide(6, 2) == 3

    def test_all_negative_division(self):
        from sample_module import abs_divide
        assert abs_divide(-6, -2) == 3

    def test_zero_division(self):
        from sample_module import abs_divide
        assert abs_divide(6, 0) == None

    def test_first_positive_second_negative_division(self):
        from sample_module import abs_divide
        assert abs_divide(6, -2) == 3

    def test_first_negative_second_positive_division(self):
        from sample_module import abs_divide
        assert abs_divide(-6, 2) == 3

if __name__ == "__main__":
    unittest.main()
