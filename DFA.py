import json


class State:
    id_counter = 0
    states = []

    def __init__(self, is_start, is_end):
        self.id = State.id_counter
        self.is_end = is_end
        self.is_start = is_start
        self.states.append(self)
        State.id_counter += 1

    @classmethod
    def get_state_by_id(cls, id):
        for state in State.states:
            if state.id == id:
                return state
        return None

    def serialize(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self, f)
        f.close()

    @classmethod
    def deserialize(cls, file_name):
        pass


class Transition:
    id_counter = 0
    transitions = []

    def __init__(self, src_state, dst_state, symbols):
        self.id = Transition.id_counter
        self.src_state = src_state
        self.dst_state = dst_state
        self.symbols = symbols
        Transition.transitions.append(self)
        Transition.id_counter += 1

    def serialize(self):
        pass

    def deserialize(self):
        pass


class DFA:
    instance = None
    start_state = State.get_state_by_id(0)

    def __init__(self):
        if DFA.instance is not None:
            self.current_state = DFA.start_state
            DFA.instance = self

    def get_next_state(self, symbol):
        for transition in Transition.transitions:
            if transition.src_state.id == self.current_state.id and symbol in transition.symbols:
                return transition.dst_state

    def is_end_state(self):
        return self.current_state.is_end
