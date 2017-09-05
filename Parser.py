class Parser:
    def __init__(self):
        self.__Automata = {} #dict of State -> input -> State
        self.__entry = None # will be one state
        self.__Accepting = [] # array of states
        self.__accepted = None

    def add_transition(self, state, input_symbol, end_state):
        self.__Automata[state][input_symbol] = end_state

    def add_state(self, state):
        print("Adding the state")
        self.__Automata[state] = {}

    def delete_state(self, state):
        del self.__Automata[state]
        if state == self.__entry:
            self.__entry = None

    def set_entry(self, state):
        old_state = self.__entry
        if old_state == state:
            self.__entry = None
        else:
            self.__entry = state
        return old_state

    def add_accepting(self, state):
        self.__Accepting.append(state)

    def remove_accepting(self, state):
        #TODO: add exceptional case handling.
        self.__Accepting.pop(self.__Accepting.index(state))

    def parse_input(self, input_word): # returns true if accepted, else False
        if not self.__entry:
            raise LookupError("Machine Must Have Entry Point")
        current_state = self.__Automata[self.__entry]
        for char in input_word:
            next_state = current_state.get(char, None)
            if not next_state:
                return False
            current_state = self.__Automata[next_state]
        return current_state in self.__Accepting
