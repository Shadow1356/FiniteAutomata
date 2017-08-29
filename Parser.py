

class Parser:
    def __init__(self):
        self.__Automata = {} #dict of State -> input -> State
        self.__entry = None # will be on state
        self.__Accepting = [] # array of states

    def add_transition(self, state, input_symbol, end_state):
        self.__Automata[state][input_symbol] = end_state

    def add_state(self, state):
        self.__Automata[state] = {}

    def delete_state(self, state):
        del self.__Automata[state]

    def set_entry(self, state):
        self.__entry = state

    def add_accepting(self, state):
        self.__Accepting.append(state)

    def remove_accepting(self, state):
        #TODO: add exceptional case handling.
        self.__Accepting.pop(self.__Accepting.index(state))

    def parse_input(self, input_word):
        pass