from tkinter import *

class FAgui:
    def __init__(self):
        self.root = None
        self.h = None
        self.w = None
        self.drawingCanvas = None

    def run(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.h = self.root.winfo_screenheight()
        self.w = self.root.winfo_screenwidth()
        self.root.wm_title("Finite Automata Simulator")
        Label(self.root, text="TEST").grid(row=0, column=1)
        Label(self.root, text="SECOND").grid(row=0, column=2)
        print(self.h, "  ", self.w)
        self.drawingCanvas = Canvas(self.root, bg='gray', width=self.w, height=700)
        self.drawingCanvas.grid(row=0, column=4, sticky=W+E+N+S)
        self.drawingCanvas.create_line(0,0,200,100)
        self.root.mainloop()


if __name__ == "__main__":
    instance = FAgui()
    instance.run()