class SymbolTable:
    instance = None

    def __init__(self):
        if SymbolTable.instance is None:
            SymbolTable.instance = self
            self.symbol_table = []
            self.keywords = ['if', 'else', 'void', 'int',
                             'while', 'break', 'switch', 'default',
                             'case', 'return', 'endif']

    def add_symbol(self, symbol):
        if symbol not in self.symbol_table:
            self.symbol_table.append(symbol)

    def write_file(self):
        f = open("symbol_table.txt", "w")
        counter = 1
        for symbol in self.keywords:
            f.write(str(counter) + '.\t' + symbol + '\n')
            counter += 1
        for ident in self.symbol_table:
            f.write(str(counter) + '.\t' + ident + '\n')
            counter += 1
        # for no in range(1, len(self.symbol_table)+1):
        #     f.write(str(no) + '.\t' + self.symbol_table[no-1] + '\n')
        f.close()
