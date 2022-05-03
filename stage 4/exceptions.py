class DuplicateTermException(Exception):
    def __init__(self, term):
        self.term = term

    def __str__(self):
        return f'The term "{self.term}" already exists. Try again:'


class DuplicateDefException(Exception):
    def __init__(self, defin):
        self.defin = defin

    def __str__(self):
        return f'The definition "{self.defin}" already exists. Try again:'
