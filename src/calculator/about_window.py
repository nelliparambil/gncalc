from tkinter import *

class AboutWindow:
    def __init__(self, msg):
        self.window = Tk()
        self.window.withdraw()
        self.window.title(msg)
        self.window.geometry('500x500')
        #self.window.configure(bg='#34A2FE')

        self.lblCalculatorName = Label(self.window, text="GN Calculator")
        self.lblCalculatorName.pack()        
        #self.lblCalculatorName.grid(row=0, column=0)
        self.lblVersion = Label(self.window, text="Version: V0.1")
        self.lblVersion.pack()
        #self.lblVersion.grid(row=1, column=0)
        self.lblAuthor = Label(self.window, text="Author : Ganesh Nelliparambil")
        self.lblAuthor.pack()
        #self.lblAuthor.grid(row=2, column=0)

    def run(self):
        self.window.deiconify()
        self.window.mainloop()
        
