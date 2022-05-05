from controller import add, remove, exit_app, ask, import_file, export_file, logging, \
    hardest_card, reset_stats
from logger import log


def menu():
    while True:
        print(log("Input the action (add, remove, import, export, "
                  "ask, exit, log, hardest card, reset stats):"))
        move = log(input())
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
        elif move == "log":
            logging()
        elif move == "hardest card":
            hardest_card(cards)
        elif move == "reset stats":
            reset_stats(cards)


def main():
    menu()


if __name__ == "__main__":
    cards = {}
    main()
