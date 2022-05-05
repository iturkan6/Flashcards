from exceptions import DuplicateCardException, DuplicateDefException, NoSuchCardException


def check_duplicates(cards, card=None, definition=None):
    if card in cards:
        raise DuplicateCardException(card)
    for i in cards.values():
        if definition == i[0]:
            raise DuplicateDefException(defin=definition)


def check_card_exist(cards, card):
    if card not in cards:
        raise NoSuchCardException(card)
