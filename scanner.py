class Scanner:
    instance = None

    def __init__(self):
        if Scanner.instance is None:
            Scanner.instance = self

    def get_next_token(self):
        return


if __name__ == '__main__':
    print('Hey!')
