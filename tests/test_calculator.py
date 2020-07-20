import unittest
import sys
import os

import tkinter as tk
from os.path import dirname, abspath, join

# Add required directories to the path
CURRENT_DIR = dirname(__file__)
CALC_DIR = abspath(join(CURRENT_DIR, '../src/', 'calculator'))
sys.path.append(CALC_DIR)

from calculator import Calculator

# To fix problem with "TclError: no display name and no $DISPLAY environment variable"
#if os.environ.get('DISPLAY','') == '':
#    print('no display found. Using :0.0')
#    os.environ.__setitem__('DISPLAY', ':0.0')


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
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

    def test_ac_clears_all_vars(self):
        self.calc.on_click_ac()
        self.assertEqual(self.calc.str_left_operand, '')
        self.assertEqual(self.calc.str_right_operand, '')
        self.assertEqual(self.calc.str_pending_operation, '')
        self.assertEqual(self.calc.str_last_result, '')

    def test_one_click_sign_button_is_plus(self):
        self.calc.on_click_sign()
        self.assertEqual(self.calc.disp_text.get(), '+')

    def test_two_clicks_sign_button_is_minus(self):
        self.calc.on_click_sign()
        self.calc.on_click_sign()
        self.assertEqual(self.calc.disp_text.get(), '-')        




if __name__ == "__main__":
    unittest.main()        