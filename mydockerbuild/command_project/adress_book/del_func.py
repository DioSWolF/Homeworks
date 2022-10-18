from .сlass import AdressBook, Record
from .show_find_logic import rec_list_print, find_contact
def error_chose(*_):
    return  "\n>>> You chose invalid <<<\n"\
            "     >>>Try again <<<\n"

def del_help_menu():
    help_text = "\nList of commands to delete:\n"
    i = 1
    for help_com in HELP_DEL_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n") 
        i += 1
    return help_text

def delete_func(book:AdressBook):
    user_input = ""
    while True:
        print("\n> 1) Some fields in contact\n> 2) Contact\n")
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose your command number: ").strip()
        if user_input == "0":
            return 
        user_input = DEL_DICT.get(user_input, error_chose)
        user_input = user_input(book)
        if user_input != None:
            print(user_input)
    

def del_contact(book: AdressBook):
    rec_find = find_contact(book)
    if rec_find == "0":
        return 
    user_ansver = input("\n<<< Do you want delet this contact? Chose Yes/Y to delete contact, else exit to the menu: ")
    if user_ansver.lower() == "yes" or user_ansver.lower() == "y":
        del book[rec_find.name.value]
    else:
        return "\n >>> Contact don`t delete <<<"
    return "\n>>> Contact deleted <<<"

def del_fields(book: AdressBook):
    rec_find = find_contact(book)
    if rec_find == "0":
        return 
    while rec_find != "0":
        print(del_help_menu())
        user_input = input(">>> 0: To enter the contact menu.\n\n<<< Select what you want to delete in a contact: ")
        if user_input == "0":
            return  
        user_input = DELETE_FUNC_DICT.get(user_input, error_chose)
        user_input = user_input(book, rec_find)
    return 

def del_phone(book: AdressBook, rec: Record):
    print(rec_list_print(rec))
    user_input = ""
    while user_input != "0":
        if rec.phone == []:
            print(">>> This contact don`t have phones <<<")
            return
        i = 1
        phone_text = "\n"
        for phone in rec.phone:
            phone_text += "".join(f"> {i}) {phone.value}") + "\n"
            i += 1
        print(phone_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number phone that you want to change: ").strip()
        if user_input == "0":
            return
        chose_phone = int(user_input) - 1
        del rec.phone[chose_phone]
        print("\n>>> Phone deleted <<<\n")
    return 

def del_email(book: AdressBook, rec: Record):
    print(rec_list_print(rec))
    user_input = ""
    while user_input != "0":
        if rec.email == []:
            print(">>> This contact don`t have email <<<")
            return
        i = 1
        email_text = "\n"
        for email in rec.email:
            email_text += "".join(f"> {i}) {email.value}") + "\n"
            i += 1
        print(email_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number email that you want to change: ").strip()
        if user_input == "0":
            return
        chose_email = int(user_input) - 1
        del rec.email[chose_email]
        print("\n>>> Email deleted <<<\n")
    
def del_adress(book: AdressBook, rec: Record):
    print(rec_list_print(rec))
    user_input = ""
    while user_input != "0":
        if user_input == "0":
            return  
        if rec.ardess_live == []:
            print(">>> This contact don`t have adress <<<")
            return
        i = 1
        adress_text = "\n"
        for email in rec.ardess_live:
            adress_text += "".join(f"> {i}) {email.value}") + "\n"
            i += 1
        print(adress_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number adress that you want to change: ").strip()
        if user_input == "0":
            return
        chose_adress = int(user_input) - 1
        del rec.ardess_live[chose_adress]
        print("\n>>> Adress deleted <<<\n")
    
def del_birthday(book: AdressBook, rec: Record):
    if rec.birthday.value == "":
        print("\n>>> This contact don`t have birthday date <<<")
    else:
        rec.birthday.value = ""
    return "\n>>> Birthday date deleted <<<\n"

def del_notes(book: AdressBook, rec: Record):
    if rec.notes.value == "":
        print("\n>>> This contact don`t have notes <<<")
    else:
        rec.notes = ""
    return "\n>>> Notes deleted <<<\n"

DEL_DICT =     { 
                    "1" : del_fields,
                    "2" : del_contact,
                    }

HELP_DEL_DICT =     {
                    "1" : "Phone in contact",
                    "2" : "Email in contact",
                    "3" : "Adress in contact",
                    "4" : "Birthday date in contact",
                    "5" : "Notes in contact",
                    }
DELETE_FUNC_DICT = {
                    "1" : del_phone,
                    "2" : del_email,
                    "3" : del_adress,
                    "4" : del_birthday,
                    "5" : del_notes,
                    }