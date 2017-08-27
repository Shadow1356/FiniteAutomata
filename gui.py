from tkinter import *

def main():
    canvas_window = CanvasWindow()

class ControlWindow:
    def __init__(self):
        self.root = None
        self.state_entry = None
        self.add_button = None

    def on_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def run(self):
        self.root = Toplevel()
        self.root.title("Finite Automata Controls")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        canvas = Canvas(self.root, borderwidth=0, background="#ffffff")
        frame = Frame(canvas, background="grey")
        vsb = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw")
        frame.bind("<Configure>", lambda event, canvas=canvas: self.on_frame_configure(canvas))
        self.state_entry = Entry(frame, width=50).grid(row=0,  column=0)
        self.add_button = Button(frame, width=8, text="Add State").grid(row=0, column=1)




class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        self.config(width=self.width, height=self.height)
        self.scale("all", 0, 0, wscale, hscale)


class CanvasWindow:
    def __init__(self):
        self.root = None
        self.frame = None
        self.drawingCanvas = None
        self.control_window = ControlWindow()
        self.run()

    def run(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)
        h = self.root.winfo_screenheight()
        w = self.root.winfo_screenwidth()
        self.root.wm_title("Finite Automata Simulator")
        self.drawingCanvas = ResizingCanvas(self.frame, width=w/2, height=h/2, bg="gray", highlightthickness=0)
        self.drawingCanvas.pack(fill=BOTH, expand=YES)
        self.drawingCanvas.create_line(0,0,200,100)
        self.drawingCanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        oval = self.drawingCanvas.create_oval(200, 25, 150, 75, fill="blue")
        print(self.drawingCanvas.coords(oval))
        self.drawingCanvas.addtag_all("all")
        self.control_window.run()
        self.root.mainloop()


if __name__ == "__main__":
    main()
