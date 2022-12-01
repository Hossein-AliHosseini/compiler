class Errors:
    instance = None

    def __init__(self):
        if Errors.instance is None:
            Errors.instance = self
            self.errors = {}

    def add_error(self, error, lineno):
        self.errors.get(lineno).append(error)

    def write_file(self):
        f = open("lexical_errors.txt", "w")
        for lineno in self.errors:
            f.write(lineno + '.\t')
            for error in self.errors[lineno]:
                f.write(error + ' ')
            f.write('\n')
        f.close()
