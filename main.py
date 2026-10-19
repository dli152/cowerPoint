import tkinter as tk
import tkinter.ttk as ttk

def destroyinsideparent(parent):
    for child in parent.winfo_children():
        child.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CowerPoint")
        self.geometry("800x600")
        self.ribbon = ttk.Frame(self)
        self.slideStrip = ttk.Frame(self)
        self.slideView = ttk.Frame(self)
        self.slideCanvas = tk.Canvas(self.slideView)
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.fileMenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.config = {}
        self.ribbonBtns = {}
        self.ribbonBtnsObj = {}

        self.ribbon.pack(side=tk.TOP, fill=tk.X)
        self.slideStrip.pack(side=tk.LEFT, fill=tk.Y)
        self.slideView.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.slideCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


app = App()
app.mainloop()