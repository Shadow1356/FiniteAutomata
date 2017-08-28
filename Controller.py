from CanvasWindow import CanvasWindow
from ControlWindow import ControlWindow
from tkinter import *
from State import State

class __Controller:
    def __init__(self, canvas_object):
        self.states = []
        self.main_window, self.canvas_window = canvas_object.setup()
        self.control_window = ControlWindow()
        self.main()

    def main(self):
        self.control_window.run()
        self.control_window.add_button.configure(width=8, command=self.add_state, text="Add State")
        # self.control_window.frame.bind("<Return>", self.add_state)
        self.main_window.mainloop()

    def add_state(self):
        new_state_name = self.control_window.state_entry.get()
        print(new_state_name)
        self.control_window.state_entry.delete(0, END)
        self.states.append(State(self.control_window.frame, new_state_name))
        new_state = self.states[-1]
        for column_number, prop in enumerate(new_state):
            prop.grid(row=len(self.states), column=column_number, sticky=W)

controller = __Controller(CanvasWindow())

