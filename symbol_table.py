class SymbolTable:
    instance = None

    def __init__(self):
        if SymbolTable.instance is None:
            SymbolTable.instance = self
            self.symbol_table = []

    def add_identifier(self, identifier):
        if identifier.get('lexeme') not in self.symbol_table:
            self.symbol_table.append(identifier)

    def write_file(self):
        f = open("symbol_table.txt", "w")
        for no in range(1, self.symbol_table+1):
            f.write(str(no) + '.\t' + self.symbol_table[no-1].get('lexeme') + '\n')
        f.close()
