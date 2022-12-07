from mymodel import RecordBD
from .add_cont_func import add_contact
from .change_cont_func import change_contact
from .del_func import delete_func
from datetime import datetime, timedelta
from connect_db import session
from .show_find_logic import show_all, find_similar

def close(*_):
    return  "\n>>> You chose invalid <<<\n"\
            "    >>>Try again <<<"


def menu_help():
    
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n") 
        i += 1
    return help_text


def parse_birthday():

    user_days = input("\n>>> 0: Exit to main menu.\n\n<< Enter the number of days to set the period for birthday showing list: ")
    print_list = ""

    if user_days == "0":
        return 

    now = datetime.now().date()

    try:
        find_day = datetime(year=now.year, month = now.month, day = now.day).date() + timedelta(days=int(user_days))
    except ValueError:
        find_day = datetime(year=now.year, month = now.month, day = now.day).date() + timedelta(days=int(user_days))

    record = session.query(RecordBD).filter(RecordBD.birthday_user <= find_day).all()
    i = 0

    for rec in record:
        print_list += f"\n> {i}) Name: {rec.name}, Birthday date: {rec._birthday_user}"
        i += 1

    return print_list


def main():
    user_input = ""
    while user_input not in STOP_WORD:
        print(menu_help())
        user_input = input(">>> 0: To exit in main menu.\n\n<< Chose your command number: ").strip()
        command_func = FUNC.get(user_input, close)
        command_func = command_func()
        if command_func != None:
            print(command_func)


def close_bot(*_):
    return "\n    <<< Good bye! >>>\n"


STOP_WORD = ("0","stop", "exit", "good bye")


FUNC = {    
        "0" : close_bot,    
        "1" : add_contact,                        
        "2" : change_contact,               
        "3" : delete_func,                                                    
        "4" : find_similar,                             
        # "5" : show,                             
        "5" : show_all,
        "6" : parse_birthday,                        
        }   


HELP_DICT = {   
            "add_contact" : "Add new contact",                  # add {name} *{phones} {birthday}
            "change_contact" : "Change contact",                # change {name} {phone}
            "delete_func" : "Delete contact",                # delete {name}                   
            "find" : "Find similar",                    # find {text}
            # "show" : "Show contact",                    # show {number}
            "show_all" : "Show all contacts",           # show all   
            "parse_birthday": "Show contact`s birthday dates"    
            }   


def start_bot():
    main()
    
