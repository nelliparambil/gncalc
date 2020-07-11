# Calculator Class
from about_window import AboutWindow
from tkinter import *

class Calculator(Frame):
    def __init__(self, master):
        #.geometry('500x500')
        super(Calculator, self).__init__(master)
        self.master = master
        self.init_calculator_gui()


    def init_calculator_gui(self):    
        self.master.title("Calculator")
        self.master.geometry('500x500')

        # Menubar -------------------------------------------------------------
        # File Menu
        self.menubar = Menu(self.master)                        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # About Menu
        self.about = AboutWindow("Calculator")
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about.run)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.master.config(menu=self.menubar)

        # Calculator Display --------------------------------------------------
        # Container for Calculator Display
        self.disp_container = Frame(self.master, bg="#505450", padx=10, 
                pady=10, relief=SUNKEN)
        self.disp_container.pack()
        # Variable for updating calculator display
        self.disp_text = StringVar()
        self.disp_text.trace(mode="w", callback=self.set_display_text)
        # Calculator display entry
        self.calc_display = Entry(self.disp_container, 
                textvariable = self.disp_text, width=100)
        self.calc_display.pack()


    def set_display_text(self):
        try:
            self.calc_display.config({"background": self.calc_display.get()})
        except:
            self.calc_display.config({"background": "0"})


'''
        # Pack in main container
        self_container = Frame(self)
        self_container.pack()


        # Calculator display
        self.disp_container = Frame(self_container)
        self.disp_container.pack()
        self.display = Label(self.disp_container)
        #self.display.configure(bg="white", width=50, height=5)
        self.display.configure(bg="white")
        #self.display.pack()
        self.display.grid(row=0, column=0)
        self.disp_container.grid_rowconfigure(0, weight=1)
        self.disp_container.grid_columnconfigure(0, weight=1)


        # Grid for buttons
        self.btn_container = Frame(self_container)
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

        for i in range(4):
            self.btn_container.grid_rowconfigure(i, weight=1)
        for i in range(4):    
            self.btn_container.grid_columnconfigure(i, weight=1)                   
'''


if __name__ == "__main__":    
    root = Tk()
    calc = Calculator(root)
    root.mainloop()


