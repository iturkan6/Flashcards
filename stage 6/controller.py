import json
import random

from check_exceptions import check_duplicates, check_card_exist
from exceptions import DuplicateCardException, DuplicateDefException, NoSuchCardException
from logger import log, logger


def add(cards: dict):
    print(log("The card:"))
    while True:
        card = log(input())
        try:
            check_duplicates(cards, card=card)
            break
        except DuplicateCardException as e:
            print(log(e))
    print(log("The definition of the card:"))
    while True:
        definition = log(input())
        try:
            check_duplicates(cards, definition=definition)
            break
        except DuplicateDefException as e:
            print(log(e))
    cards[card] = [definition, 0]
    print(log(f'The pair ("{card}":"{definition}") has been added.'))


def remove(cards: dict):
    print(log("Which card?"))
    card = log(input())
    try:
        check_card_exist(cards, card)
        del cards[card]
        print(log("The card has been removed."))
    except NoSuchCardException as e:
        print(log(e))


def exit_app():
    print(log("Bye bye!"))


def import_file(cards: dict):
    print(log("File name:"))
    file_name = log(input())
    try:
        with open(file_name, "r") as file:
            new_cards = json.loads(file.read())
            cards.update(new_cards)
            print(log(f"{len(new_cards)} cards have been loaded."))
    except FileNotFoundError:
        print(log("File not found."))


def export_file(cards: dict):
    print(log("File name:"))
    file_name = log(input())
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json.dumps(cards, indent=4))
    print(log(f"{len(cards)} cards have been saved."))


def ask(cards: dict):
    print(log("How many times to ask?"))
    repetitions = int(log(input()))
    for i in range(repetitions):
        card = random.choice(list(cards.keys()))
        print(log(f'Print the definition of "{card}":'))
        answer = log(input())
        right_answer = cards.get(card)
        if answer == right_answer[0]:
            print(log("Correct!"))
            continue
        another_key = [k for k, v in cards.items() if v[0] == answer]
        if another_key:
            print(
                log(f'Wrong. The right answer is "{right_answer[0]}", '
                    f'but your definition is correct for "{another_key[0]}".'))
            right_answer[1] += 1
        else:
            print(log(f'Wrong. The right answer is "{right_answer[0]}".'))
            right_answer[1] += 1


def logging():
    print(log("File name:"))
    file = log(input())
    with open(file, "w", encoding="utf-8") as f:
        f.write(str(logger))
    print(log("The log has been saved."))


def hardest_card(cards: dict):
    max_ = 0
    res = []
    for k, v in cards.items():
        if v[1] > max_:
            res.clear()
            res.append(k)
            max_ = v[1]
        elif v[1] == max_ and v[1] != 0:
            res.append(k)
    if len(res) == 1:
        print(log('The hardest card is "{}". '
                  'You have {} errors answering it'.format(*res, max_)))
    elif len(res) > 1:
        print(log('The hardest cards are "{}".  You have {} errors answering them.'.format([i for i in res], max_)))
    else:
        print(log("There are no cards with errors."))


def reset_stats(cards: dict):
    for v in cards.values():
        v[1] = 0
    print(log("Card statistics have been reset."))
