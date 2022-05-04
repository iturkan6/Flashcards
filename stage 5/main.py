from controller import add, import_file, export_file, exit_app, remove, ask


def menu():
    while True:
        move = input("Input the action (add, remove, import, export, ask, exit):\n")
        if move == "add":
            add(cards)
        elif move == "remove":
            remove(cards)
        elif move == "exit":
            exit_app()
            break
        elif move == "ask":
            ask(cards)
        elif move == "import":
            import_file(cards)
        elif move == "export":
            export_file(cards)


def main():
    menu()


if __name__ == "__main__":
    cards = {}
    main()
