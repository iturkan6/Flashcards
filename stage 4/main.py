from exceptions import DuplicateDefException, DuplicateTermException


def collect_data():
    c_num = int(input("Input the number of cards:\n"))
    for i in range(1, c_num + 1):
        print(f"The term for card #{i}:")
        while True:
            term = input()
            try:
                check_duplicates(term=term)
                break
            except DuplicateTermException as ex:
                print(ex)
        print(f'The definition for card #{i}:')
        while True:
            definition = input()
            try:
                check_duplicates(definition=definition)
                break
            except DuplicateDefException as ex:
                print(ex)
        cards[term] = definition


def check_duplicates(term=None, definition=None):
    if term in cards:
        raise DuplicateTermException(term)
    if definition in cards.values():
        raise DuplicateDefException(definition)


def check_answer():
    for t, d in cards.items():
        answer = input(f'Print the definition of "{t}":\n')
        if d == answer:
            print("Correct!")
            continue
        another_key = [k for k, v in cards.items() if v == answer]
        if another_key:
            print(f'Wrong. The right answer is "{d}", but your definition is correct for "{another_key}".')
        else:
            print(f'Wrong. The right answer is "{d}".')


if __name__ == "__main__":
    cards = {}
    collect_data()
    check_answer()
