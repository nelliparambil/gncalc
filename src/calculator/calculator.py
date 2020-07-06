# Calculator Class
from calculator.about_window import AboutWindow
from tkinter import *

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')

        # Menubar
        self.menubar = Menu(self.root)                        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.about = AboutWindow("GN Calculator")
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about.run)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menubar)

        # Pack in main container
        self.root_container = Frame(self.root)
        self.root_container.pack()


        # Calculator display
        self.disp_container = Frame(self.root_container)
        self.disp_container.pack()
        self.entry = Entry(self.disp_container)
        self.entry.pack()


        # Grid for buttons
        self.btn_container = Frame(self.root_container)
        self.btn_container.pack()

        btn_percent = Button(self.btn_container, text="%")
        btn_percent.grid(row=0, column=0)
        btn_divide = Button(self.btn_container, text="/")
        btn_divide.grid(row=0, column=1)
        btn_multi = Button(self.btn_container, text="*")
        btn_multi.grid(row=0, column=2)
        btn_subtract = Button(self.btn_container, text="-")
        btn_subtract.grid(row=0, column=3)
        btn_clear = Button(self.btn_container, text="C")
        btn_clear.grid(row=0, column=4)
        btn_seven = Button(self.btn_container, text="7")
        btn_seven.grid(row=1, column=0)
        btn_eight = Button(self.btn_container, text="8")
        btn_eight.grid(row=1, column=1)
        btn_nine = Button(self.btn_container, text="9")
        btn_nine.grid(row=1, column=2)
        btn_add = Button(self.btn_container, text="+")
        btn_add.grid(row=1, column=3)
        btn_ac = Button(self.btn_container, text="AC")
        btn_ac.grid(row=1, column=4)
        btn_four = Button(self.btn_container, text="4")
        btn_four.grid(row=2, column=0)
        btn_five = Button(self.btn_container, text="5")
        btn_five.grid(row=2, column=1)
        btn_six = Button(self.btn_container, text="6")
        btn_six.grid(row=2, column=2)
        btn_openbrace = Button(self.btn_container, text="(")
        btn_openbrace.grid(row=2, column=3)
        btn_one = Button(self.btn_container, text="1")
        btn_one.grid(row=3, column=0)
        btn_two = Button(self.btn_container, text="2")
        btn_two.grid(row=3, column=1)
        btn_three = Button(self.btn_container, text="3")
        btn_three.grid(row=3, column=2)
        btn_equals = Button(self.btn_container, text="=")
        btn_equals.grid(row=3, column=3)
        btn_closebrace = Button(self.btn_container, text=")")
        btn_closebrace.grid(row=3, column=4)
        btn_zero = Button(self.btn_container, text="0")
        btn_zero.grid(row=4, column=0)
        btn_comma = Button(self.btn_container, text=",")
        btn_comma.grid(row=4, column=1)
        btn_plusorminus = Button(self.btn_container, text="+/-")
        btn_plusorminus.grid(row=4, column=2)                        

    def run(self):
        self.root.mainloop()





