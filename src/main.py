from tkinter import Tk

from os.path import dirname, abspath, join
import sys 

# Add required directories to the path
CURRENT_DIR = dirname(__file__)
CALC_DIR = abspath(join(CURRENT_DIR, 'calculator'))
sys.path.append(CALC_DIR)

from calculator import Calculator

if __name__ == "__main__":    
    root = Tk()
    calc = Calculator(root)
    root.mainloop()

