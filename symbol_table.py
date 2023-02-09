class SymbolTable:
    instance = None

    def __init__(self):
        if SymbolTable.instance is None:
            SymbolTable.instance = self
            self.symbol_table = {
                'symbol': [],
                'addr': [],
                'type': [],
            }
            self.keywords = ['if', 'else', 'void', 'int',
                             'while', 'break', 'switch', 'default',
                             'case', 'return', 'endif']

    @classmethod
    def get_instance(cls):
        if SymbolTable.instance is None:
            SymbolTable()
        return SymbolTable.instance

    def add_symbol(self, symbol: str):
        if symbol not in self.symbol_table['symbol']:
            self.symbol_table['symbol'].append(symbol)
            self.symbol_table['addr'].append(-1)
            self.symbol_table['type'].append('')

    def set_symbol_addr(self, symbol: str, addr: int):
        found = False
        for i in range(len(self.symbol_table['symbol'])):
            if self.symbol_table['symbol'][i] == symbol:
                self.symbol_table['addr'][i] = addr
                found = True
                break
        return found

    def set_symbol_type(self, symbol: str, s_type: str):
        found = False
        for i in range(len(self.symbol_table['symbol'])):
            if self.symbol_table['symbol'][i] == symbol:
                self.symbol_table['type'][i] = s_type
                found = True
                break
        return found

    def get_symbol_addr(self, symbol: str) -> int:
        for i in range(len(self.symbol_table['symbol'])):
            if self.symbol_table['symbol'][i] == symbol:
                return self.symbol_table['addr'][i]
        return -1

    def get_symbol_type(self, symbol: str) -> str:
        for i in range(len(self.symbol_table['symbol'])):
            if self.symbol_table['symbol'][i] == symbol:
                return self.symbol_table['type'][i]
        return ''

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
