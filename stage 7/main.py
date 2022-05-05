import argparse

from controller import add, remove, exit_app, ask, import_file, export_file, logging, \
    hardest_card, reset_stats
from logger import log


def menu():
    file_from = args.import_from
    if file_from:
        import_file(cards, file_from)
    while True:
        print(log("Input the action (add, remove, import, export, "
                  "ask, exit, log, hardest card, reset stats):"))
        move = log(input())
        if move == "add":
            add(cards)
        elif move == "remove":
            remove(cards)
        elif move == "ask":
            ask(cards)
        elif move == "import":
            print(log("File name:"))
            file = log(input())
            import_file(cards, file)
        elif move == "export":
            print(log("File name:"))
            file = log(input())
            export_file(cards, file)
        elif move == "log":
            logging()
        elif move == "hardest card":
            hardest_card(cards)
        elif move == "reset stats":
            reset_stats(cards)
        elif move == "exit":
            exit_app()
            file_to = args.export_to
            if file_to:
                export_file(cards, file_to)
            break


def main():
    menu()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--import_from")
    parser.add_argument("--export_to")
    args = parser.parse_args()
    cards = {}
    main()
