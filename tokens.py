class Tokens:
    instance = None

    def __init__(self):
        if Tokens.instance is None:
            self.tokens = {}
            Tokens.instance = self

    def add_token(self, token, lineno):
        if self.tokens.get(lineno) is None:
            self.tokens[lineno] = []
        self.tokens.get(lineno).append(token)

    def write_file(self):
        f = open("tokens.txt", "w")
        for lineno in self.tokens:
            f.write(str(lineno) + '.\t')
            for token in self.tokens[lineno]:
                f.write(str(token).replace('"', '').replace("'", "") + ' ')
            f.write('\n')
        f.close()
