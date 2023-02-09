import collections
from symbol_table import SymbolTable


class CodeGenerator:

    def __init__(self):
        self.action_func = {
            '6': self.declare_var_action,
            '7': self.declare_arr_action,
            '28': self.pop_expression_action,
            '31': self.jpf_action,
            '32': self.jp_action,
            '42': self.assign_action,
            '45': self.p_arr_action,
            '46': self.operation_action,
            '50': self.operation_action,
            '54': self.operation_action,
            '62': self.call_func_action,
            '67': self.p_operation_action,
            '68': self.p_num_action,
            '69': self.push,  # p_type
            '70': self.p_id_action,
            '71': self.push,
            '72': self.declare_fun_action,
            '73': self.p_num_temp_action,
            '74': self.save_action,
            '75': self.jpf_save_action,
            '80': self.jpf_action,
        }
        self.semantic_stack = []
        self.program_block = {}
        self.last_var_addr = 500
        self.current_program_line = 0
        self.symbol_table = SymbolTable.get_instance()

    def increase_last_addr(self, amount: int):
        self.last_var_addr += amount

    # get temp variable
    def get_temp_var(self):
        last_addr = self.last_var_addr
        self.increase_last_addr(4)
        return last_addr

    def top(self, i):
        return self.semantic_stack[len(self.semantic_stack) - 1 - i]

    def push(self, element):
        self.semantic_stack.append(element)

    def pop(self):
        if len(self.semantic_stack) > 0:
            return self.semantic_stack.pop()
        else:
            return None

    def dump_program_block(self):
        sorted_program_block = sorted(self.program_block)
        f = open("output.txt", "w")
        for key in sorted_program_block:
            f.write(f'{key}\t')
            f.write(self.program_block[key])
            f.write('\n')
        f.close()

    def call_func_action(self):
        func_arg_addr = self.pop()
        func_addr = self.pop()
        if func_addr == -1:
            self.program_block[self.current_program_line] = f'(PRINT, {func_arg_addr},   ,   )'
            self.current_program_line += 1
        self.push(func_addr)

    def p_arr_action(self):
        arr_arg = self.pop()
        arr_addr = self.pop()
        arr_addr += 4 * arr_arg
        self.push(arr_addr)

    def pop_expression_action(self):
        self.pop()

    def assign_action(self):
        self.program_block[self.current_program_line] = f'(ASSIGN, {self.top(0)}, {self.top(1)},   )'
        self.current_program_line += 1
        self.pop()

    def operation_action(self):
        t = self.get_temp_var()
        self.program_block[self.current_program_line] = f'({self.top(1)}, {self.top(2)}, {self.top(0)}, {t})'
        self.current_program_line += 1
        self.pop()
        self.pop()
        self.pop()
        self.push(t)

    def p_id_action(self, token: str):
        symbol_addr = self.symbol_table.get_symbol_addr(token)
        self.push(symbol_addr)

    def p_num_temp_action(self, token: str):
        token = '#' + token
        self.push(token)

    def p_num_action(self, token: str):
        num = int(token)
        self.push(num)

    def p_operation_action(self, token: str):
        tmp = ''
        if token == '+':
            tmp = 'ADD'
        elif token == '-':
            tmp = 'SUB'
        elif token == '*':
            tmp = 'MULT'
        elif token == '/':
            tmp = 'DIV'
        elif token == '<':
            tmp = 'LT'
        elif token == '==':
            tmp = 'EQ'
        self.push(tmp)

    def save_action(self):
        self.push(self.current_program_line)
        self.current_program_line += 1

    def jp_action(self):
        self.program_block[self.top(0)] = f'(JP, {self.current_program_line},   ,   )'
        self.pop()

    def jpf_action(self):
        self.program_block[self.top(0)] = f'(JPF, {self.top(1)}, {self.current_program_line},   )'
        self.pop()
        self.pop()

    def jpf_save_action(self):
        self.program_block[self.top(0)] = f'(JPF, {self.top(1)}, {self.current_program_line + 1},   )'
        self.pop()
        self.pop()
        self.push(self.current_program_line)
        self.current_program_line += 1

    def declare_var_action(self):
        symbol_id = self.pop()
        symbol_type = self.pop()
        if symbol_type == 'int':
            self.program_block[self.current_program_line] = f'(ASSIGN, #0, {self.last_var_addr},   )'
            self.symbol_table.set_symbol_addr(symbol_id, self.last_var_addr)
            self.symbol_table.set_symbol_type(symbol_id, 'int')
            self.increase_last_addr(4)
            self.current_program_line += 1

    def declare_arr_action(self):
        arr_len = self.pop()
        arr_addr = self.pop()
        arr_type = self.pop()
        if arr_type == 'int':
            self.program_block[self.current_program_line] = f'(ASSIGN, #0, {arr_addr},   )'
            self.increase_last_addr(4 * arr_len)
            self.current_program_line += 1

    def declare_fun_action(self):
        self.pop()
        self.pop()
        self.pop()

    def while_action(self):
        self.program_block[self.top(0)] = f'(JPF, {self.top(1)}, {self.current_program_line + 1},   )'
        self.program_block[self.current_program_line] = f'(JP, {self.top(2)}, ,   )'
        self.current_program_line += 1
        self.pop()
        self.pop()
        self.pop()
        # todo: break

    def break_action(self):
        pass

    def code_gen(self, action_num: str, token: str):
        func = self.action_func.get(action_num, None)
        if func is not None:
            if action_num in ['45', '67', '68', '69', '70', '71', '73']:
                func(token)
            else:
                func()
