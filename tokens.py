class Tokens:
    instance = None

    def __init__(self):
        if Tokens.instance is None:
            Tokens.instance = self
            self.tokens = {}

    def add_token(self, token, lineno):
        self.tokens.get(lineno).append(token)

    def write_file(self):
        f = open("tokens.txt", "w")
        for lineno in self.tokens:
            f.write(lineno + '.\t')
            for token in self.tokens[lineno]:
                f.write(token + ' ')
            f.write('\n')
        f.close()
