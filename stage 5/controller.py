import json
import random

from check_exceptions import check_duplicates, check_card_exist
from exceptions import DuplicateDefException, DuplicateCardException, NoSuchCardException


def add(cards: dict):
    print("The card:")
    while True:
        card = input()
        try:
            check_duplicates(cards, card=card)
            break
        except DuplicateCardException as e:
            print(e)
    print("The definition of the card:")
    while True:
        definition = input()
        try:
            check_duplicates(cards, definition=definition)
            break
        except DuplicateDefException as e:
            print(e)
    cards[card] = definition
    print(f'The pair ("{card}":"{definition}") has been added.')


def remove(cards: dict):
    card = input("Which card?\n")
    try:
        check_card_exist(cards, card)
        del cards[card]
        print("The card has been removed.")
    except NoSuchCardException as e:
        print(e)


def exit_app():
    print("Bye bye!")


def import_file(cards: dict):
    file_name = input("File name:\n")
    try:
        with open(file_name, "r") as file:
            new_cards = json.loads(file.read())
            cards.update(new_cards)
            print(f"{len(new_cards)} cards have been loaded.")
    except FileNotFoundError:
        print("File not found.")


def export_file(cards: dict):
    file_name = input("File name:\n")
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json.dumps(cards, indent=4))
    print(f"{len(cards)} cards have been saved.")


def ask(cards: dict):
    repetitions = int(input("How many times to ask?\n"))
    for i in range(repetitions):
        card = random.choice(list(cards.keys()))
        answer = input(f'Print the definition of "{card}":\n')
        right_answer = cards.get(card)
        if answer == right_answer:
            print("Correct!")
            continue
        another_key = [k for k, v in cards.items() if v == answer]
        if another_key:
            print(f'Wrong. The right answer is "{right_answer}", but your definition is correct for "{another_key}".')
        else:
            print(f'Wrong. The right answer is "{right_answer}".')
