"""
AmirHossein Barati - 99101308
Behzad Nabavi - 99109817
MohammadHossein AliHosseini - 99101921
"""

from scanner import Scanner


class Compiler:
    def __init__(self):
        self.scanner = Scanner("input.txt")

    def scan(self):
        while True:
            if not self.scanner.get_next_token():
                break
        self.scanner.tokens.write_file()
        self.scanner.errors.write_file()
        self.scanner.symbol_table.write_file()

    def compile(self):
        pass


compiler = Compiler()
compiler.scan()
