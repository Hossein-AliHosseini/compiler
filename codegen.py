from symbol_table import SymbolTable


class CodeGenerator:

    def __init__(self):
        self.action_symbols = {
            'p_id': '70',
            
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

    def code_gen(self, action_num: int, token: str):
        if action_num == self.action_symbols['p_id']:
            self.p_id_action(token)
