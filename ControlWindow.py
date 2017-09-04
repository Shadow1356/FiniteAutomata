from tkinter import *

class ControlWindow:
    def __init__(self):
        self.root = None
        self.state_entry = None
        self.add_button = None
        self.frame = None
        self.input_entry = None
        self.input_button = None

    def on_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def run(self):
        self.root = Toplevel()
        self.root.title("Finite Automata Controls")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        my_canvas = Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame = Frame(my_canvas, background="grey")
        vsb = Scrollbar(self.root, orient="vertical", command=my_canvas.yview)
        my_canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        my_canvas.pack(side="left", fill="both", expand=True)
        my_canvas.create_window((4,4), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda event, canvas=my_canvas: self.on_frame_configure(canvas))
        self.state_entry = Entry(self.frame)
        self.state_entry.grid(row=0,  column=0)
        self.add_button = Button(self.frame)
        self.add_button.grid(row=0, column=1)
        self.input_entry = Entry(self.frame)
        self.input_entry.grid(row=0, column=2)
        self.input_button = Button(self.frame)
        self.input_button.grid(row=0, column=3)
