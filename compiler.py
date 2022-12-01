from scanner import Scanner


class Compiler:
    def __init__(self):
        self.scanner = Scanner("input.txt")

    def scan(self):
        while (True):
            if not self.scanner.get_next_token():
                break
        self.scanner.tokens.write_to_file()
        self.scanner.errors.write_to_file()
        self.scanner.symbol_table.write_to_file()

    def compile(self):
        pass

compiler = Compiler()
compiler.scan()