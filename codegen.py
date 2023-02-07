from symbol_table import SymbolTable


class CodeGenerator:

    def __init__(self):
        self.action_func = {
            '70': self.p_id_action
        }
        self.semantic_stack = []
        self.program_block = []
        self.last_var_addr = 500
        self.current_program_line = 1
        self.symbol_table = SymbolTable()

    # get temp variable
    def get_temp_var(self):
        last_addr = self.last_var_addr
        self.last_var_addr += 1
        return last_addr

    def top(self, i):
        return self.program_block[len(self.program_block) - 1 - i]

    def push(self, element):
        self.semantic_stack.append(element)

    def pop(self):
        if len(self.semantic_stack) > 0:
            return self.semantic_stack.pop()
        else:
            return None

    def write_code_at_index(self, index: int, code: str):
        if len(self.program_block) < index:
            raise Exception
        elif len(self.program_block) == index:
            self.program_block.append(code)
        else:
            self.program_block[index] = code

    # TODO: dump program block to file
    def dump_program_block(self):
        pass

    def p_id_action(self, token: str):
        tmp = self.symbol_table.get_symbol(token)
        self.push(tmp)

    def save(self):
        self.push(self.current_program_line)
        self.current_program_line += 1

    def jpf_save(self):
        self.program_block[self.top(0)] = (self.top(1), self.current_program_line + 1)
        self.pop()
        self.pop()
        self.push(self.current_program_line)
        self.current_program_line += 1

    def code_gen(self, action_num: str, token: str):
        func = self.action_func[action_num]
        if action_num == '70':
            func(token)
        else:
            func()
