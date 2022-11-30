class Tokens:
    instance = None

    def __init__(self):
        if Tokens.instance is None:
            Tokens.instance = self
            file = open("tokens.txt", "w")

    def add_token(self, token):
        pass
