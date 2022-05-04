from exceptions import DuplicateCardException, DuplicateDefException, NoSuchCardException


def check_duplicates(cards, card=None, definition=None):
    if card in cards:
        raise DuplicateCardException(card)
    if definition in cards.values():
        raise DuplicateDefException(definition)


def check_card_exist(cards, card):
    if card not in cards:
        raise NoSuchCardException(card)
