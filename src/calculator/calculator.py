# Calculator Class
from about_window import AboutWindow
from tkinter import *

class Calculator(Frame):
    def __init__(self, master=None):
        super(Calculator, self).__init__(master)

        self.master = master
        self.init_calculator_gui()
        self.str_left_operand = ''
        self.str_right_operand = ''
        self.str_pending_operation = ''
        self.str_last_result = '' 


    def init_calculator_gui(self):    
        if self.master != None:                
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

        if self.master != None:                           
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
                textvariable=self.disp_text, height=2, width=48, anchor='e',
                padx=10, font='Helvetica 16 bold')                
        self.calc_display.pack()

        # Calculator Keypad ---------------------------------------------------
        # Container for Calculator Keypad
        self.keypad_container = Frame(self.master, padx=5, 
                pady=5, relief=RAISED)
        self.keypad_container.pack()
        # Calculator keys
        btn_percent = Button(self.keypad_container, text="%", height=2, 
                width=5, command=lambda: self.on_click_operator('%'))
        btn_percent.grid(row=0, column=0, padx=(3,1), 
                pady=(3,1), sticky=W+E+S+N)
        btn_divide = Button(self.keypad_container, text="/", height=2,
                width=5, command=lambda: self.on_click_operator('/'))        
        btn_divide.grid(row=0, column=1, sticky=W+E)
        btn_multi = Button(self.keypad_container, text="*", height=2,
                width=5, command=lambda: self.on_click_operator('*'))
        btn_multi.grid(row=0, column=2, padx=(3,1), 
                pady=(3,1), sticky=W+E+S+N)
        btn_subtract = Button(self.keypad_container, text="-", height=2,
                width=5, command=lambda: self.on_click_operator('-'))        
        btn_subtract.grid(row=0, column=3, padx=(3,1), 
                pady=(3,1), sticky=W+E+S+N)
        btn_clear = Button(self.keypad_container, text="C", height=2,
                width=5, bg="#d65a29", 
                command=lambda: self.disp_text.set("0"))        
        btn_clear.grid(row=0, column=4, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_seven = Button(self.keypad_container, text="7", height=2,
                width=5, command=lambda: self.on_click_digit('7'))
        btn_seven.grid(row=1, column=0, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_eight = Button(self.keypad_container, text="8", height=2,
                width=5, command=lambda: self.on_click_digit('8'))        
        btn_eight.grid(row=1, column=1, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_nine = Button(self.keypad_container, text="9", height=2,
                width=5, command=lambda: self.on_click_digit('9'))        
        btn_nine.grid(row=1, column=2, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_add = Button(self.keypad_container, text="+", height=5,
                width=5, command=lambda: self.on_click_operator('+'))        
        btn_add.grid(row=1, column=3, padx=(3,1), pady=(3,1), 
                rowspan=2, sticky=W+E+S+N)
        btn_ac = Button(self.keypad_container, text="AC", height=2,
                width=5, command=lambda: self.on_click_ac())        
        btn_ac.grid(row=1, column=4,padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_four = Button(self.keypad_container, text="4", height=2,
                width=5, command=lambda: self.on_click_digit('4'))        
        btn_four.grid(row=2, column=0, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_five = Button(self.keypad_container, text="5", height=2,
                width=5, command=lambda: self.on_click_digit('5'))
        btn_five.grid(row=2, column=1, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_six = Button(self.keypad_container, text="6", height=2,
                width=5, command=lambda: self.on_click_digit('6'))        
        btn_six.grid(row=2, column=2, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_openbrace = Button(self.keypad_container, text="(", height=2,
                width=5, command=lambda: self.on_click_symbol('('))        
        btn_openbrace.grid(row=2, column=4, padx=(3,1), 
                pady=(3,1), sticky=W+E+S+N)
        btn_one = Button(self.keypad_container, text="1", height=2,
                width=5, command=lambda: self.on_click_digit('1'))        
        btn_one.grid(row=3, column=0, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_two = Button(self.keypad_container, text="2", height=2,
                width=5, command=lambda: self.on_click_digit('2'))        
        btn_two.grid(row=3, column=1, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_three = Button(self.keypad_container, text="3", height=2,
                width=5, command=lambda: self.on_click_digit('3'))        
        btn_three.grid(row=3, column=2, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_equals = Button(self.keypad_container, text="=", height=5,
                width=5, command=lambda: self.on_click_result())        
        btn_equals.grid(row=3, column=3, padx=(3,1), pady=(3,1), 
                rowspan=2, sticky=W+E+S+N)
        btn_closebrace = Button(self.keypad_container, text=")", height=2,
                width=5, command=lambda: self.on_click_symbol(')'))        
        btn_closebrace.grid(row=3, column=4, padx=(3,1), 
                pady=(3,1), sticky=W+E+S+N)
        btn_zero = Button(self.keypad_container, text="0", height=2,
                width=15, command=lambda: self.on_click_digit('0'))        
        btn_zero.grid(row=4, column=0, padx=(3,1), pady=(3,1), 
                columnspan=2, sticky=W+E+S+N)
        btn_dot = Button(self.keypad_container, text=".", height=2,
                width=5, command=lambda: self.on_click_digit('.'))        
        btn_dot.grid(row=4, column=2, padx=(3,1), pady=(3,1), sticky=W+E+S+N)
        btn_plusorminus = Button(self.keypad_container, text="+/-", height=2,
                width=5, command=lambda: self.on_click_symbol('+/-'))        
        btn_plusorminus.grid(row=4, column=4, padx=(3,1), 
                pady=(3,1), sticky=W+E+S+N)
                
        for i in range(4):
            self.keypad_container.grid_rowconfigure(i, weight=1)
        for i in range(4):    
            self.keypad_container.grid_columnconfigure(i, weight=1)                   


    def on_click_digit(self, digit):
        current_diplay_text = self.disp_text.get()    
        if current_diplay_text == '0':
                self.disp_text.set(digit)
        else:
                self.disp_text.set(current_diplay_text + digit)


    def on_click_operator(self, oper):
        self.str_left_operand = self.disp_text.get()
        self.disp_text.set('0')
        self.str_pending_operation = oper

                               
    def on_click_result(self):
        self.str_right_operand = self.disp_text.get()

        f_left_operand = float(self.str_left_operand)
        f_right_operand = float(self.str_right_operand)

        if self.str_pending_operation == '+':
                f_result = f_left_operand + f_right_operand
        elif self.str_pending_operation == '-':
                f_result = f_left_operand - f_right_operand
        elif self.str_pending_operation == '/':
                f_result = f_left_operand / f_right_operand
        elif self.str_pending_operation == '*':
                f_result = f_left_operand * f_right_operand
        elif self.str_pending_operation == '%':
                f_result = f_left_operand % f_right_operand                
        else:
                pass

        self.str_last_result = str(f_result)
        self.disp_text.set(self.str_last_result)


    def on_click_symbol(self, symbol):
        pass


    def on_click_ac(self):
        self.str_left_operand = ''
        self.str_right_operand = ''
        self.str_pending_operation = ''
        self.str_last_result = ''


if __name__ == "__main__":    
    root = Tk()
    calc = Calculator(root)
    root.mainloop()


