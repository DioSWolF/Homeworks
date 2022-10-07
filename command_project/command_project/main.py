from typing import Callable, Dict
from clean_bot.clean_bot import start_clean_bot
from adress_book.adressbook_bot import start_bot
from notes_window.notes_bot import start_bot as start_notes

book = None

def adress_book_bot():
    start_bot()

def sorted_bot():
    start_clean_bot()

def notes_bot():
    start_notes()


def exit_handler():  
    raise SystemExit('\n<<< Good bye!>>>\n')

COMMAND_HANDLERS: Dict[str, Callable] = {
    '0': exit_handler,
    '1': adress_book_bot,
    '2': notes_bot,
    '3': sorted_bot
    }

HELP_DICT = {
    '1': 'Menu adress book',
    '2': 'Menu notes',
    '3': 'Menu sorted'
}

def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n") 
        i += 1
    return help_text

def parse_user_input(user_input: str):
    command = COMMAND_HANDLERS.get(user_input)
    if command != None:     
        return command()
    return ('\n >>> Unknown command <<<')

def main():
    while True:
        print(menu_help())
        user_input = input('>>> 0: Exit to main menu\n\n<< Enter the command: ').strip()
        resalt = None
        try:
            resalt = parse_user_input(user_input)
            if resalt != None:
                print(resalt)
        except SystemExit as e:
            if resalt != None:
                print(e)
            break

if __name__ == "__main__":
    main()
