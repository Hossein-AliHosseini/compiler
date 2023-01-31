from DFA import DFA
from errors import Errors
from symbol_table import SymbolTable
from tokens import Tokens


class Scanner:
    def __init__(self, code_file):
        self.file = open(code_file)
        self.end_of_file = False
        self.symbol_table = SymbolTable()
        self.tokens = Tokens()
        self.dfa = DFA()
        self.dfa.deserialize('dfa/DFA.json')
        self.errors = Errors()
        self.line_no = 1
        self.is_rewind = False
        self.lookahead_char = None

    def get_char(self):
        if self.is_rewind:
            self.is_rewind = False
            return self.lookahead_char
        if self.end_of_file:
            return None
        c = self.file.read(1)
        self.lookahead_char = c
        if not c:
            self.end_of_file = True
        return c

    @staticmethod
    def is_whitespace(char):
        return char in [' ', '\t', '\n', '\r', '\v', '\f']

    def get_next_token(self):
        last_char = None
        buffer = ''
        self.dfa.reset()
        while not self.dfa.is_final():
            last_char = self.get_char()
            if self.end_of_file:
                return 'EOF', '$', self.line_no
            if last_char is None:
                break
            appended = '' if last_char == '\n' else last_char
            buffer += appended
            if not self.dfa.can_move_current_state(last_char):
                self.errors.add_error((buffer, 'Invalid input'), self.line_no)
                self.line_no += 1 if last_char == '\n' else 0
                return self.get_next_token()
        if self.dfa.is_look_ahead():
            buffer = buffer[:-1] if last_char != '\n' else buffer
            self.is_rewind = True
            last_char = None
        self.line_no += 1 if last_char == '\n' else 0
        if not self.dfa.is_final():
            if self.dfa.get_type() == 'COMMENT':
                message = buffer[:min(7, len(buffer))]
                message += '...' if len(buffer) > 7 else ''
                self.errors.add_error((message, 'Unclosed comment'), self.line_no)
            return self.get_next_token()
        if self.dfa.is_error():
            self.errors.add_error((buffer, self.dfa.get_error_type()), self.line_no)
            return self.get_next_token()
        token_type = 'KEYWORD' if buffer in self.symbol_table.keywords else self.dfa.get_type()
        if token_type != 'WHITESPACE' and token_type != 'COMMENT':
            self.tokens.add_token((token_type, buffer), self.line_no)
        if token_type == 'ID':
            self.symbol_table.add_symbol(buffer)
        return token_type, buffer, self.line_no
