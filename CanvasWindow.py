from tkinter import *
from ResizingCanvas import ResizingCanvas

class CanvasWindow:
    def __init__(self):
        self.root = None
        self.frame = None
        self.drawingCanvas = None


    def setup(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)
        h = self.root.winfo_screenheight()
        w = self.root.winfo_screenwidth()
        self.root.wm_title("Finite Automata Simulator")
        self.drawingCanvas = ResizingCanvas(self.frame, width=w/2, height=h/2, bg="gray", highlightthickness=0)
        self.drawingCanvas.pack(fill=BOTH, expand=YES)
        # self.drawingCanvas.create_line(0,0,200,100)
        # self.drawingCanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # oval = self.drawingCanvas.create_oval(200, 25, 150, 75, fill="blue")
        # print(self.drawingCanvas.coords(oval))
        self.drawingCanvas.addtag_all("all")
        return self.root, self.drawingCanvas
