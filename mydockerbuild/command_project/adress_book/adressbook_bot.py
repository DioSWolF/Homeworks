from .сlass import AdressBook, Iterable
from .add_cont_func import add_contact
from .show_find_logic import show, show_all, find
from .change_cont_func import change_contact
from .del_func import delete_func
from datetime import datetime

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except FileNotFoundError:

#             with open("data.bin", "rb") as file:
#                 return pickle.load(file)
#     return inner

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

def parse_birthday(book:AdressBook):
    user_days = input("\n>>> 0: Exit to main menu.\n\n<< Enter the number of days to set the period for birthday showing list: ")

    if user_days == "0":
        return 

    now = datetime.now()
    j = 1
    print_list = ""

    Iterable(book)
    for items in book:
        rec, str_info = items
        rec = book[rec]

        i = 0
        I = 0
        zero_day = now.day
        month_december = now.month
        new_year = now.year
        try:
            user_days = int(user_days)
        except ValueError:
            return "\n>>> You wrote text, I need number! <<<"
        while i <= user_days:

            try:
                date_birthday = (datetime(year=now.year, month =rec.birthday.value.month, day = rec.birthday.value.day)).strftime("%d %m")
                find_day = (datetime(year = new_year, month = month_december, day = zero_day + I)).strftime("%d %m")

            except ValueError:
                if month_december == 12:
                    month_december = 0
                    new_year += 1
                
                month_december += 1
                zero_day = 0
                I = 0
            except AttributeError:
                break

            if find_day == date_birthday:
                print_list += f"\n> {j}) Name: {rec.name.value}, Birthday date: {rec.birthday.value.strftime('%A, %d %B %Y')}"
                j += 1
                break
            i += 1            
            I += 1
    return print_list



def main():
    user_input = ""
    while user_input not in STOP_WORD:
        print(menu_help())
        user_input = input(">>> 0: To exit in main menu.\n\n<< Chose your command number: ").strip()
        command_func = FUNC.get(user_input, close)
        command_func = command_func(book)
        if command_func != None:
            print(command_func)
    book.save_data()

def close_bot(*_):
    return "\n    <<< Good bye! >>>\n"

STOP_WORD = ("0","stop", "exit", "good bye")

FUNC = {    
        "0" : close_bot,    
        "1" : add_contact,                        
        "2" : change_contact,               
        "3" : delete_func,                                                    
        "4" : find,                             
        "5" : show,                             
        "6" : show_all,
        "7" : parse_birthday,                        
        }   

HELP_DICT = {   
            "add_contact" : "Add new contact",                  # add {name} *{phones} {birthday}
            "change_contact" : "Change contact",                # change {name} {phone}
            "delete_func" : "Delete contact",                # delete {name}                   
            "find" : "Find similar",                    # find {text}
            "show" : "Show contact",                    # show {number}
            "show_all" : "Show all contacts",           # show all   
            "parse_birthday": "Show contact`s birthday dates"    
            }   

def start_bot():
    global book
    book = AdressBook()
    book.load_data()    
    main()
    
# if __name__ == "__main__":
#     book = AdressBook()
#     book.load_data()    
#     main()


# def parse_date(user_input):
#     date_input = re.findall(r"\d{2}[ /.,\\]\d{2}[ /.,\\]\d{4}", user_input)
#     if len(date_input) > 0:
#         return date_input[-1] 
#     else:
#         return user_input
