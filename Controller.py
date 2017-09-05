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
        self.parser = Parser()
        self.main()

    def main(self):
        self.control_window.run()
        self.control_window.add_button.configure(width=8, command=self.add_state, text="Add State")
        self.control_window.input_button.configure(width=8, command=self.parse, text="Input")
        # self.control_window.frame.bind("<Return>", self.add_state)
        self.main_window.mainloop()

    def parse(self):
        input_word = self.control_window.input_entry.get()
        self.control_window.input_entry.delete(0, END)
        try:
            result = self.parser.parse_input(input_word)
        except LookupError as le:
            print(le)
        else:
            if result:
                print("This machine accepts ", input_word)
            else:
                print("This machine does not accept ", input_word)

    def add_state(self):
        new_state_name = self.control_window.state_entry.get()
        print(new_state_name)
        self.control_window.state_entry.delete(0, END)
        self.states.append(State(self.control_window.frame, new_state_name))
        new_state = self.states[-1]
        new_state.state_label.grid(row=len(self.states), column=0)
        new_state.transition_button.configure(text="TRANSITION", command=lambda : self.transition(new_state))
        new_state.transition_button.grid(row=len(self.states), column=1)
        new_state.delete_button.configure(text="DELETE", command=lambda : self.delete_state(new_state))
        new_state.delete_button.grid(row=len(self.states), column=2)
        new_state.accept_button.configure(text="ACCEPT", command=lambda : self.make_accepting(new_state))
        new_state.accept_button.grid(row=len(self.states), column=3)
        new_state.entry_button.configure(text="--->", command=lambda : self.make_entry(new_state))
        new_state.entry_button.grid(row=len(self.states), column=4)
        self.parser.add_state(new_state)


    def transition(self, state):
        print("Transition Fired")
        # Popup(??) to input transition

    def delete_state(self, state):
        print("Delete Fired")
        self.parser.delete_state(state)
        for prop in state:
            prop.grid_forget()
        del self.states[self.states.index(state)]

    def make_accepting(self, state):
        print("Accept Fired")
        self.parser.add_accepting(state)

    def make_entry(self, state):
        print("Entry Fired")
        old_entry = self.parser.set_entry(state)
        state.entry_button.configure(bg="blue")
        try:
            old_entry.entry_button.configure(bg="light grey")
        except AttributeError as ae:
            print(ae)
            print("No return value")


if __name__ == "__main__":
    controller = __Controller(CanvasWindow())

