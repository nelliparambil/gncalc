import unittest
import sys
import os

from tkinter import Tcl
from os.path import dirname, abspath, join

# Add required directories to the path
CURRENT_DIR = dirname(__file__)
CALC_DIR = abspath(join(CURRENT_DIR, '../src/', 'calculator'))
sys.path.append(CALC_DIR)

from calculator import Calculator

# To fix problem with "TclError: no display name and no $DISPLAY environment variable"
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = Tcl()
        self.root.loadtk()
        self.calc = Calculator(self.root)        


    def test_multiple_digit_clicks(self):
        self.calc.on_click_digit('9')
        self.calc.on_click_digit('0')
        self.calc.on_click_digit('3')
        self.calc.on_click_digit('1')
        self.assertEqual(self.calc.disp_text.get(), '9031')

    def test_ingores_zero_infront(self):
        self.calc.on_click_digit('0')
        self.calc.on_click_digit('0')
        self.calc.on_click_digit('4')
        self.calc.on_click_digit('0')
        self.assertEqual(self.calc.disp_text.get(), '40')

    def test_appends_dot(self):
        self.calc.on_click_digit('1')
        self.calc.on_click_digit('.')
        self.calc.on_click_digit('5')
        self.assertEqual(self.calc.disp_text.get(), '1.5')


if __name__ == "__main__":
    unittest.main()        