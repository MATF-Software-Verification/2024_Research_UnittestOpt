import pytest
import os
import sys

# Add the current directory to the path so Python can find the module
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from sample_module import multiply

def test_multiply_positive():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-1, -1) == 1

def test_multiply_zero():
    assert multiply(0, 5) == 0

def test_multiply_redundant():
    assert multiply(2, 3) == 6  # Redundant
    assert multiply(0, 5) == 0  # Redundant

if __name__ == '__main__':
    pytest.main()
