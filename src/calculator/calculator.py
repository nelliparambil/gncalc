# Calculator Class
from about_window import AboutWindow
from tkinter import *

class Calculator(Frame):
    def __init__(self, master):
        super(Calculator, self).__init__(master)
        self.master = master
        self.init_calculator_gui()


    def init_calculator_gui(self):    
        self.master.title("Calculator")
        self.master.geometry('350x350')

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
        self.disp_container = Frame(self.master, padx=5, 
                pady=5, relief=SUNKEN)
        self.disp_container.pack()
        # Variable for updating calculator display
        self.disp_text = StringVar()
        self.disp_text.set('0')
        # Calculator display entry
        self.calc_display = Label(self.disp_container, bg='black',
                textvariable=self.disp_text, height=2, width=100)                
        self.calc_display.pack()

        # Calculator Keypad ---------------------------------------------------
        # Container for Calculator Keypad
        self.keypad_container = Frame(self.master, padx=5, 
                pady=5, relief=RAISED)
        self.keypad_container.pack()
        # Calculator keys
        btn_percent = Button(self.keypad_container, text="%", height=2, 
                width=5, command=lambda: self.update_display_text('%'))
        btn_percent.grid(row=0, column=0, padx=(3,1), pady=(3,1))
        btn_divide = Button(self.keypad_container, text="/", height=2,
                width=5, command=lambda: self.update_display_text('/'))        
        btn_divide.grid(row=0, column=1)
        btn_multi = Button(self.keypad_container, text="*", height=2,
                width=5, command=lambda: self.update_display_text('*'))
        btn_multi.grid(row=0, column=2, padx=(3,1), pady=(3,1))
        btn_subtract = Button(self.keypad_container, text="-", height=2,
                width=5, command=lambda: self.update_display_text('-'))        
        btn_subtract.grid(row=0, column=3, padx=(3,1), pady=(3,1))
        btn_clear = Button(self.keypad_container, text="C", height=2,
                width=5, bg="#d65a29", 
                command=lambda: self.update_display_text('C'))        
        btn_clear.grid(row=0, column=4, padx=(3,1), pady=(3,1))
        btn_seven = Button(self.keypad_container, text="7", height=2,
                width=5, command=lambda: self.update_display_text('7'))
        btn_seven.grid(row=1, column=0, padx=(3,1), pady=(3,1))
        btn_eight = Button(self.keypad_container, text="8", height=2,
                width=5, command=lambda: self.update_display_text('8'))        
        btn_eight.grid(row=1, column=1, padx=(3,1), pady=(3,1))
        btn_nine = Button(self.keypad_container, text="9", height=2,
                width=5, command=lambda: self.update_display_text('9'))        
        btn_nine.grid(row=1, column=2, padx=(3,1), pady=(3,1))
        btn_add = Button(self.keypad_container, text="+", height=5,
                width=5, command=lambda: self.update_display_text('+'))        
        btn_add.grid(row=1, column=3, padx=(3,1), pady=(3,1), rowspan=2)
        btn_ac = Button(self.keypad_container, text="AC", height=2,
                width=5, command=lambda: self.update_display_text('AC'))        
        btn_ac.grid(row=1, column=4,padx=(3,1), pady=(3,1))
        btn_four = Button(self.keypad_container, text="4", height=2,
                width=5, command=lambda: self.update_display_text('4'))        
        btn_four.grid(row=2, column=0, padx=(3,1), pady=(3,1))
        btn_five = Button(self.keypad_container, text="5", height=2,
                width=5, command=lambda: self.update_display_text('5'))
        btn_five.grid(row=2, column=1, padx=(3,1), pady=(3,1))
        btn_six = Button(self.keypad_container, text="6", height=2,
                width=5, command=lambda: self.update_display_text('6'))        
        btn_six.grid(row=2, column=2, padx=(3,1), pady=(3,1))
        btn_openbrace = Button(self.keypad_container, text="(", height=2,
                width=5, command=lambda: self.update_display_text('('))        
        btn_openbrace.grid(row=2, column=4, padx=(3,1), pady=(3,1))
        btn_one = Button(self.keypad_container, text="1", height=2,
                width=5, command=lambda: self.update_display_text('1'))        
        btn_one.grid(row=3, column=0, padx=(3,1), pady=(3,1))
        btn_two = Button(self.keypad_container, text="2", height=2,
                width=5, command=lambda: self.update_display_text('2'))        
        btn_two.grid(row=3, column=1, padx=(3,1), pady=(3,1))
        btn_three = Button(self.keypad_container, text="3", height=2,
                width=5, command=lambda: self.update_display_text('3'))        
        btn_three.grid(row=3, column=2, padx=(3,1), pady=(3,1))
        btn_equals = Button(self.keypad_container, text="=", height=5,
                width=5, command=lambda: self.update_display_text('='))        
        btn_equals.grid(row=3, column=3, padx=(3,1), pady=(3,1), rowspan=2)
        btn_closebrace = Button(self.keypad_container, text=")", height=2,
                width=5, command=lambda: self.update_display_text(')'))        
        btn_closebrace.grid(row=3, column=4, padx=(3,1), pady=(3,1))
        btn_zero = Button(self.keypad_container, text="0", height=2,
                width=15, command=lambda: self.update_display_text('0'))        
        btn_zero.grid(row=4, column=0, padx=(3,1), pady=(3,1), columnspan=2)
        btn_comma = Button(self.keypad_container, text=",", height=2,
                width=5, command=lambda: self.update_display_text(','))        
        btn_comma.grid(row=4, column=2, padx=(3,1), pady=(3,1))
        btn_plusorminus = Button(self.keypad_container, text="+/-", height=2,
                width=5, command=lambda: self.update_display_text('+/-'))        
        btn_plusorminus.grid(row=4, column=4, padx=(3,1), pady=(3,1))    
        
        for i in range(4):
            self.keypad_container.grid_rowconfigure(i, weight=1)
        for i in range(4):    
            self.keypad_container.grid_columnconfigure(i, weight=1)                   
        

    def update_display_text(self, text):
        self.disp_text.set(text)

'''


'''


if __name__ == "__main__":    
    root = Tk()
    calc = Calculator(root)
    root.mainloop()


