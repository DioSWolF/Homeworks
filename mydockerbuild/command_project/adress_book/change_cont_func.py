from .сlass import Record, AdressBook, Name, Phone, Birthday, Email, AdressLive, Notes
from .add_cont_func import write_ardess, write_email, write_phone
from .show_find_logic import find_contact, rec_list_print


def change_contact(book:AdressBook):
    rec_find = ""
    while rec_find not in STOP_WORD:
        rec_find = find_contact(book)
        if rec_find == "0":
            return

        if isinstance(rec_find, Record):
            return take_contact(book, rec_find)
        print(rec_find)

def take_contact(book: AdressBook, rec: Record) -> None:
    user_chose = ""

    while user_chose not in STOP_WORD:
        print(rec_list_print(rec, rec.name))
        user_chose = input(">> 7: Add new contact\n\n<< Select the field number to change it: ").strip()
        user_chose = CHANGE_FUNC_DICT.get(str(user_chose), error_chose)
        user_chose = user_chose(book, rec)
        if user_chose != None:
            user_chose

        book.add_record(rec)
        book.save_data()
    return

def change_name(book: AdressBook, rec:Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write new name: ").strip()

    if user_input == "0":
        return 
    if len(user_input) < 1:
        return "\n>>> You write invalid new name! <<<\n" \
               "     >>> Name not change! <<<"

    old_rec = rec.name.value
    rec.name = Name(user_input)
    book.add_record(rec)
    del book[old_rec]
    return

def add_phone(book:AdressBook, rec:Record): 
    write_phone(rec)
    return "\n>>> Phone added <<<"

def chose_phone(book: AdressBook, rec:Record) -> None:
    user_input = ""
    while True:
        rec.phone = list(filter(lambda i: i.value != "", rec.phone))
        if rec.phone == []:
            print("\n>>> You need to added phone <<<")
            write_phone(rec)
        i = 1
        phone_text = "\n"
        for phone in rec.phone:
            phone_text += "".join(f"> {i}) {phone.value}") + "\n"
            i += 1
        if phone_text == "\n":
            return
        print(phone_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number phone that you want to change: ").strip()
        if user_input == "0":
            return
        chose_phone = int(user_input) - 1
        chose_phone = change_phone(rec, chose_phone)
        if chose_phone != None:
            print(chose_phone)

    

def change_phone(rec:Record, chose_old_phone:str) -> None:
    new_phone = input("\n>>> 0: To enter the contact menu.\n\n<< Write new phone: ").strip()
    if new_phone == "0":
        return
    if len(new_phone.split(" ")) >= 2:
        return "\n>>> You write invalid new phone! <<<\n" \
               "     >>> Phone not change! <<<"
    rec.phone[chose_old_phone] = Phone(new_phone)
    rec.phone = list(filter(lambda i: i.value != "", rec.phone))

    return "\n>>> Phone change <<<"

def chose_email(book: AdressBook, rec:Record) -> None:
    user_input = ""
    while True:
        rec.email = list(filter(lambda i: i.value != "", rec.email))
        if rec.email == []:
            print("\n>>> You need to added email <<<")
            write_email(rec)
        i = 1
        email_text = "\n"
        for email in rec.email:
            email_text += "".join(f"> {i}) {email.value}") + "\n"
            i += 1
        if email_text == "\n":
            return
        print(email_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number email that you want to change: ").strip()
        if user_input == "0":
            return
        chose_email = int(user_input) - 1
        chose_email = change_email(rec, chose_email)
        if chose_email != None:
            print(chose_email)
    

def change_email(rec:Record, chose_old_email:str) -> None:
    new_email = input("\n>>> 0: To enter the contact menu.\n\n<< Write new email: ").strip()
    if new_email == "0":
        return
    if len(new_email.split(" ")) >= 2:
        return "\n>>> You write invalid new email! <<<\n" \
               "     >>> Email not change! <<<"
    rec.email[chose_old_email] = Email(new_email)
    rec.email = list(filter(lambda i: i.value != "", rec.email))
    return "\n>>> Email change <<<"

def chose_adress(book: AdressBook, rec:Record) -> None:
    user_input = ""
    while True:
        rec.ardess_live = list(filter(lambda i: i.value != "", rec.ardess_live))
        if rec.ardess_live == []:
            print("\n>>> You need to added adress <<<")
            write_ardess(rec)
        i = 1
        adress_text = "\n"
        for adress in rec.ardess_live:
            adress_text += "".join(f"> {i}) {adress.value}") + "\n"
            i += 1
        if adress_text == "\n":
            return
        print(adress_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number adress that you want to change: ").strip()
        if user_input == "0":
            return
        chose_adress = int(user_input) - 1
        chose_adress = change_adress(rec, chose_adress)
        if chose_adress != None:
            print(chose_adress)
        
    
def change_adress(rec:Record, chose_old_adress:str) -> None:
    new_adress = input("\n>>> 0: To enter the contact menu.\n\n<< Write new adress: ").strip()
    rec.ardess_live[chose_old_adress] = AdressLive(new_adress)
    rec.ardess_live = list(filter(lambda i: i.value != "", rec.ardess_live))
    return "\n>>> Adress change <<<"

def change_birthday(book: AdressBook, rec:Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write new birthday date: ").strip()
    if user_input == "0":
        return 

    user_input = user_input.strip()
    birthday = Birthday(user_input)

    rec.birthday = birthday
    return None

def change_Notes(book: AdressBook, rec:Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write new name: ").strip()
    if user_input == "0":
        return 
    rec.notes = Notes(user_input)
    print("\n>>> Email change <<<")
    return


def error_chose(*_):
    return  "\n>>> You chose invalid <<<"\
            "      >>>Try again <<<\n"

def close_bot(*_):
    return "exit"

CHANGE_FUNC_DICT = {
                    "0" : close_bot,                # ready
                    "1" : change_name,              # ready
                    "2" : chose_phone,              #
                    "3" : chose_email,             #
                    "4" : chose_adress,            #
                    "5" : change_birthday,          # ready
                    "6" : change_Notes,             #
                    "7" : add_phone,
                    }
    
STOP_WORD = ("0","stop", "exit", "good bye")
                    # "2" : add_phone,