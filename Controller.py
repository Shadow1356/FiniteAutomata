from CanvasWindow import CanvasWindow
from ControlWindow import ControlWindow
from tkinter import *
from State import State
from Parser import Parser

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
        new_state.state_label.grid(row=len(self.states), column=0)
        new_state.transition_button.configure(text="TRANSITION", command=lambda : self.transition(new_state))
        new_state.transition_button.grid(row=len(self.states), column=1)
        new_state.delete_button.configure(text="X", command=lambda : self.delete_state(new_state))
        new_state.delete_button.grid(row=len(self.states), column=2)
        new_state.accept_button.configure(text="ACCEPT", command=lambda : self.make_accepting(new_state))
        new_state.accept_button.grid(row=len(self.states), column=3)
        new_state.entry_button.configure(text="--->", command=lambda : self.make_entry(new_state))
        new_state.entry_button.grid(row=len(self.states), column=4)


    def transition(self, state):
        print("Transition Fired")

    def delete_state(self, state):
        print("Delete Fired")

    def make_accepting(self, state):
        print("Accept Fired")

    def make_entry(self, state):
        print("Entry Fired")


if __name__ == "__main__":
    controller = __Controller(CanvasWindow())

