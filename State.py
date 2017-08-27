from tkinter import *


class State:
    def __init__(self, input_frame, state_name):
        self.frame = input_frame
        self.name = state_name
        self.transition_button = None
        self.delete_button = None
        self.accept_button = None
        self.entry_button = None
        self.make_state()

    def make_state(self):
        pass
