"""
AmirHossein Barati - 99101308
Behzad Nabavi - 99109817
MohammadHossein AliHosseini - 99101921
"""

from scanner import Scanner
from Parser import Parser


class Compiler:
    def __init__(self):
        self.scanner = Scanner('input.txt')
        self.parser = Parser(self.scanner)

    # def scan(self):
    #     while True:
    #         if not self.scanner.get_next_token():
    #             break
    #     self.scanner.tokens.write_file()
    #     self.scanner.errors.write_file()
    #     self.scanner.symbol_table.write_file()

    def parse(self):
        self.parser.parse()
        # self.parser.print_parse_tree()
        # self.parser.write_errors_to_file()
        # self.parser.code_generator.write_to_file()

    def compile(self):
        pass


compiler = Compiler()
compiler.parse()
