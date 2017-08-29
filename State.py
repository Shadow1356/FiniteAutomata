from tkinter import *


class State:
    def __init__(self, input_frame, state_name):
        self._frame = input_frame
        self.name = state_name
        self.transition_button = None
        self.delete_button = None
        self.accept_button = None
        self.entry_button = None
        self.state_label = None
        self._make_state()

    def _make_state(self):
        self.state_label = Label(self._frame, text=self.name)
        self.transition_button = Button(self._frame)
        self.delete_button = Button(self._frame)
        self.accept_button = Button(self._frame)
        self.entry_button = Button(self._frame)

    def __iter__(self): #minght not need.
        yield self.state_label
        yield self.transition_button
        yield self.delete_button
        yield self.accept_button
        yield self.entry_button
