import unittest
import sys

from os.path import dirname, abspath, join

# Add required directories to the path
CURRENT_DIR = dirname(__file__)
CALC_DIR = abspath(join(CURRENT_DIR, '../src/', 'calculator'))
sys.path.append(CALC_DIR)

from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_on_click_digit(self):
        self.assertEqual(1, 1)



if __name__ == "__main__":
    unittest.main()        