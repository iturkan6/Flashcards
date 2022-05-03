def collect_data():
    c_num = int(input("Input the number of cards:\n"))
    for i in range(1, c_num + 1):
        term = input(f"The term for card #{i}:\n")
        definition = input(f'The definition for card #{i}:\n')
        cards.append((term, definition))


def check_data():
    for t, d in cards:
        answer = input(f'Print the definition of "{t}":\n')
        print("Correct!" if d == answer else f'Wrong. The right answer is "{d}".')


if __name__ == "__main__":
    cards = []
    collect_data()
    check_data()
