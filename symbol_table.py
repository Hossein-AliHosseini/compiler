class SymbolTable:
    instance = None

    def __init__(self):
        if SymbolTable.instance is None:
            self.line_no = 1
            SymbolTable.instance = self
            self.last_symbol_addr = 100
            self.symbol_table = {}
            self.keywords = ['if', 'else', 'void', 'int',
                             'while', 'break', 'switch', 'default',
                             'case', 'return', 'endif']

    def add_symbol(self, symbol: str):
        if symbol not in self.symbol_table:
            symbol_addr = self.last_symbol_addr
            self.last_symbol_addr += 1
            line_no = self.line_no
            self.line_no += 1
            self.symbol_table[symbol] = (symbol_addr, line_no)

    def get_symbol(self, symbol: str):
        return self.symbol_table.get(symbol, default=None)

    def write_file(self):
        f = open("symbol_table.txt", "w")
        counter = 1
        for symbol in self.keywords:
            f.write(str(counter) + '.\t' + symbol + '\n')
            counter += 1
        for ident in self.symbol_table.values():
            f.write(str(counter) + '.\t' + ident + '\n')
            counter += 1
        f.close()
