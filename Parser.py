from anytree import Node, RenderTree
from codegen import CodeGenerator


class Parser:

    def __init__(self, scanner, grammar):
        self.code_generator = CodeGenerator()
        self.grammar = grammar
        self.scanner = scanner
        self.stack = ['0']
        self.goto_s = None
        self.set_goto_states()
        self.errors = []

    def get_next_token(self):
        while True:
            token = self.scanner.get_next_token()
            if token[0] == 'COMMENT' or token[0] == 'WHITESPACE':
                continue
            else:
                break
        return token

    @staticmethod
    def syntax_error_writer(errors):
        result = ''
        if len(errors) == 0:
            result += 'There is no syntax error.'
        else:
            for error in errors:
                result = result + str(error) + '\n'
        file = open('symbol_table.txt', 'w')
        file.write(result)

    @staticmethod
    def parse_tree_writer(parse_tree):
        file = open('parse_tree.txt', 'w')
        file.write(parse_tree[:-1])

    def parse(self):
        current_token = self.get_next_token()
        while True:
            last_index = self.stack[-1]
            key_value = self.calc_value(current_token)
            if key_value in self.grammar['parse_table'][last_index]:
                next_move = self.grammar['parse_table'][last_index][key_value].split('_')
                if next_move[0] == 'reduce':
                    self.code_generator.code_gen(next_move[1], current_token[1])
                    lhs = self.grammar['grammar'][next_move[1]][0]
                    rhs = self.grammar['grammar'][next_move[1]][2:]
                    lrn = Node(lhs)
                    if rhs != ['epsilon']:
                        start_index = len(self.stack) - 2 * len(rhs)
                        index = 0
                        while index < 2 * len(rhs):
                            popped = self.stack.pop(start_index)
                            if index % 2 == 0:
                                popped.parent = lrn
                            index += 1
                    else:
                        Node('epsilon', lrn)
                    new_move = self.grammar['parse_table'][self.stack[-1]][lhs].split('_')
                    self.stack.append(lrn)
                    if next_move[0] != 'goto':
                        self.parse_tree_writer(self.format_tree(lrn))
                    self.stack.append(new_move[1])
                elif next_move[0] == "accept":
                    Node('$', lrn)
                    self.parse_tree_writer(self.format_tree(lrn))
                    self.syntax_error_writer(self.errors)
                    return
                elif next_move[0] == 'shift':
                    if current_token:
                        node = Node((current_token[0], current_token[1]))
                    else:
                        node = Node(current_token)
                    self.stack.append(node)
                    self.stack.append(next_move[1])
                    current_token = self.get_next_token()
            else:
                error_text = "#" + str(current_token[2]) + " : syntax error , illegal " + str(current_token[1])
                self.errors.append(error_text)
                current_token = self.get_next_token()
                while self.stack[-1] not in self.goto_s:
                    self.stack.pop()
                    popped = self.stack.pop()
                    if popped.name in self.grammar['non_terminals']:
                        error_text = "syntax error , discarded " + str(popped.name) + " from stack"
                    else:
                        error_text = "syntax error , discarded (" + str(popped.name[0]) + ", " + str(
                            popped.name[1]) + ") from stack"
                    self.errors.append(error_text)
                while not self.follow_set(self.stack[-1], self.calc_value(current_token)):
                    if self.calc_value(current_token) == '$':
                        error_text = "#" + str(current_token[2]) + " : syntax error , Unexpected EOF"
                        self.errors.append(error_text)
                        self.syntax_error_writer(self.errors)
                        self.parse_tree_writer('')
                        return
                    else:
                        error_text = "#" + str(current_token[2]) + " : syntax error , discarded " + str(
                            current_token[1]) + " from input"
                        self.errors.append(error_text)
                        current_token = self.get_next_token()
                next_non_terminal = self.follow_set(self.stack[-1], self.calc_value(current_token))
                next_state = self.grammar['parse_table'][self.stack[-1]][next_non_terminal].split('_')[1]
                error_text = "#" + str(current_token[2]) + " : syntax error , missing " + str(next_non_terminal)
                self.errors.append(error_text)
                self.stack.append(Node(next_non_terminal))
                self.stack.append(next_state)

    def set_goto_states(self):
        res = []
        for state in self.grammar['parse_table'].keys():
            for letter in self.grammar['parse_table'][state].values():
                if letter.startswith('goto'):
                    res.append(state)
                    break
        self.goto_s = res

    def follow_set(self, state, token):
        res = []
        for x in self.grammar['parse_table'][state].keys():
            if self.grammar['parse_table'][state][x].startswith('goto'):
                res.append(x)
        for goto in sorted(res):
            if token in self.grammar['follow'][goto]:
                return goto
        return None

    def format_tree(self, root):
        result = ''
        for pre, fill, node in RenderTree(root):
            result += pre + self.format_node_name(node) + '\n'
        return result

    @staticmethod
    def format_node_name(node):
        return str(node.name[0] + ", " + node.name[1]) \
            if type(node.name) == tuple \
            else node.name

    @staticmethod
    def calc_value(token):
        if token[0] == 'EOF':
            return '$'
        if token[0] == 'KEYWORD' or token[0] == 'SYMBOL':
            return token[1]
        return token[0]
