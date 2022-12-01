import json


class State:

    def __init__(self, s_id, name, is_start, is_end):
        self.id = s_id
        self.name = name
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
                'whitespace_sign': 'w',
                'braces_sign': 'b',
                'eof_sign': 'e',
                'symbol_sign': 's',
                'mult_sign': '*',
                'backslash_sign': '/',
                'equal_sign': '=',
                'other_sign': 'o',
            }
            self.starting_state_id = 0
            self.states = {}
            self.transitions = {}
            self.starting_state = None
            self.current_state = None
            self.error_states_id = []
            self.look_ahead_states_id = []
            DFA.instance = self

    def get_state_by_id(self, s_id):
        return self.states.get(s_id, default=None)

    def get_transition_by_id(self, t_id):
        return self.transitions.get(t_id, default=None)

    def get_type_of_char(self, char):
        if '0' <= char <= '9':
            return self.sign_map['digit_sign']
        if char.isalpha():
            return self.sign_map['letter_sign']
        if char in [';', ':', ',', '+', '-', '<']:
            return self.sign_map['symbol_sign']
        if char in ['[', ']', '(', ')', '{', '}']:
            return self.sign_map['braces_sign']
        if char == "\n":
            return self.sign_map['newline_sign']
        if char in [' ', '\r', '\t', '\v', '\f']:
            return self.sign_map['whitespace_sign']
        return char

    def can_move_current_state(self, last_char):
        char = self.get_type_of_char(last_char)
        if char not in self.sign_map.values():
            return False
        other_transition = None
        for t_id in self.transitions:
            transition = self.get_transition_by_id(t_id)
            if transition.src_state == self.current_state and last_char in transition.symbols:
                self.current_state = transition.dst_state
                return True
            if transition.src_state == self.current_state and self.sign_map['other_sign'] in transition.symbols:
                other_transition = transition
        if other_transition is None:
            return False
        else:
            self.current_state = other_transition.dst_state
            return True

    @classmethod
    def deserialize(cls, file_name):
        with open(file_name, 'r') as f:
            data = json.loads(f.read())
            decoded_dfa = DFA()
            decoded_dfa.init_states(data)
            decoded_dfa.init_transactions(data)
            decoded_dfa.current_state = decoded_dfa.get_state_by_id(decoded_dfa.starting_state_id)
            return decoded_dfa

    def init_transactions(self, data):
        for transition in data['transitions']:
            src_state = self.get_state_by_id(transition['state_src_id'])
            dst_state = self.get_state_by_id(transition['state_dst_id'])
            symbols = transition['symbols']
            t_id = transition['id']
            self.add_transition(t_id, src_state, dst_state, symbols)

    def init_states(self, data):
        for state in data['states']:
            state_obj = self.add_state(state['id'], state['name'], state['start'], state['end'])
            if state['name'].startswith('Err'):
                self.error_states_id.append(state_obj.id)
            if state['name'].endswith('*'):
                self.look_ahead_states_id.append(state_obj.id)

    def add_state(self, s_id, name, is_start, is_end):
        state = State(s_id, name, is_start, is_end)
        self.states[s_id] = state
        return state

    def add_transition(self, t_id, src_state, dst_state, symbols):
        transition = Transition(t_id, src_state, dst_state, symbols)
        self.transitions[t_id] = transition
        return transition

    def reset(self):
        self.current_state = self.get_state_by_id(self.starting_state_id)

    def is_final(self):
        return self.current_state.is_end

    def is_error(self):
        return True if self.current_state.id in self.error_states_id else False

    def is_look_ahead(self):
        return self.current_state in self.look_ahead_states_id
