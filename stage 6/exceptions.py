class DuplicateCardException(Exception):
    def __init__(self, card):
        self.card = card

    def __str__(self):
        return f'The card "{self.card}" already exists. Try again:'


class DuplicateDefException(Exception):
    def __init__(self, defin):
        self.defin = defin

    def __str__(self):
        return f'The definition "{self.defin}" already exists. Try again:'


class NoSuchCardException(Exception):
    def __init__(self, card):
        self.card = card

    def __str__(self):
        return f'Can\'t remove "{self.card}": there is no such card.'
