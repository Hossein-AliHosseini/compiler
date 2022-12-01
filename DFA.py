import json


class State:

    def __init__(self, s_id, is_start, is_end):
        self.id = s_id
        self.is_end = is_end
        self.is_start = is_start


class Transition:

    def __init__(self, t_id, src_state, dst_state, symbols):
        self.id = t_id
        self.src_state = src_state
        self.dst_state = dst_state
        self.symbols = symbols


class DFA:
    instance = None

    def __init__(self):
        if DFA.instance is not None:
            self.sign_map = {
                'letter_sign': 'l',
                'digit_sign': 'd',
                'newline_sign': 'n',
            }
            self.states = {}
            self.transitions = {}
            self.stating_state = None
            self.current_state = None
            DFA.instance = self

    def add_state(self, s_id, is_start, is_end):
        state = State(s_id, is_start, is_end)
        self.states[s_id] = state
        return state

    def add_transition(self, t_id, src_state, dst_state, symbols):
        transition = Transition(t_id, src_state, dst_state, symbols)
        self.transitions[t_id] = transition
        return transition

    def get_state_by_id(self, s_id):
        return self.states.get(s_id, default=None)

    def get_transition_by_id(self, t_id):
        return self.transitions.get(t_id, default=None)

    @classmethod
    def deserialize(cls, file_name):
        with open(file_name, 'r') as f:
            data = json.loads(f.read())
            decoded_dfa = DFA()
            for state in data['states']:
                decoded_dfa.add_state(state['id'], state['start'], state['end'])
            for transition in data['transitions']:
                src_state = decoded_dfa.get_state_by_id(transition['state_src_id'])
                dst_state = decoded_dfa.get_state_by_id(transition['state_dst_id'])
                symbols = transition['symbols']
                t_id = transition['id']
                decoded_dfa.add_transition(t_id, src_state, dst_state, symbols)
            return decoded_dfa

    def get_next_state(self, symbol):
        for transition in Transition.transitions:
            if transition.src_state.id == self.current_state.id and symbol in transition.symbols:
                return transition.dst_state

    def is_end_state(self):
        return self.current_state.is_end
