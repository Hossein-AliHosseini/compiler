class Errors:
    instance = None

    def __init__(self):
        if Errors.instance is None:
            Errors.instance = self
            self.errors = {}

    def add_error(self, error, lineno):
        if self.errors.get(lineno) is None:
            self.errors[lineno] = []
        self.errors.get(lineno).append(error)

    def write_file(self):
        f = open("lexical_errors.txt", "w")
        if len(self.errors) == 0:
            f.write("There is no lexical error.")
        else:
            for lineno in self.errors:
                f.write(str(lineno) + '.\t')
                for error in self.errors[lineno]:
                    f.write(str(error).replace("'", "") + ' ')
                f.write('\n')
        f.close()
