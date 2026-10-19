import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmb
import tkinter.filedialog as tkfd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CowerPoint")
        self.geometry("800x600")


app = App()
app.mainloop()