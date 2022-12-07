# from .сlass import AdressBook, Record
# from .show_find_logic import rec_list_print, find_contact
from connect_db import session
from mymodel import NotesDB, RecordBD, PhoneDB, EmailDB, AddressDB
from adress_book.show_find_logic import find_contact, take_user_info


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


def delete_func():
    user_input = ""
    find_name = find_contact()
    if find_name == "0":
        return 
    while True:

        user_input = input("\n> 1) Some fields in contact\n> 2) Contact\n\n>>> 0: To enter the contact menu.\n\n<< Chose your command number: ").strip()
        if user_input == "0":
            return 
        user_input = DEL_DICT.get(user_input, error_chose)
        user_input = user_input(find_name)
        if user_input != None:
            print(user_input)

            bd_rec = session.query(RecordBD).filter_by(name=user_input).first()
            if bd_rec == None:
                return


def del_contact(rec_find):
    
    if rec_find == "0":
        return 
    user_ansver = input("\n<<< Do you want delet this contact? Chose Yes/Y to delete contact, else exit to the menu: ")
    if user_ansver.lower() == "yes" or user_ansver.lower() == "y":
        session.query(RecordBD).filter_by(name=rec_find.name).delete()
        session.commit()
    else:
        return "\n >>> Contact don`t delete <<<"
    return "\n>>> Contact deleted <<<"


def del_fields(find_cont):

    while True:
        user_dict, print_info = take_user_info(find_cont)
        print(print_info)
        user_input = input("<<< Select what you want to delete in a contact: ")
        if user_input == "0":
            return  
        user_input = DELETE_FUNC_DICT.get(user_input, error_chose)
        user_input = user_input(user_dict)



def del_phone(user_dict):
    user_input = ""
    while user_input != "0":
        if user_dict["phone"] == []:
            print(">>> This contact don`t have phones <<<")
            return
        i = 1
        phone_text = "\n"
        for phone in user_dict["phone"]:
            phone_text += "".join(f"> {i}) {phone}") + "\n"
            i += 1
        print(phone_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number phone that you want to change: ").strip()
        if user_input == "0":
            return
        chose_phone = int(user_input) - 1
        us_phone = user_dict["phone"][chose_phone]
        session.query(PhoneDB).filter_by(_phone_property=us_phone, user_id=user_dict["record"].id).delete()
        session.commit()
        del user_dict["phone"][chose_phone]
        print("\n>>> Phone deleted <<<\n")
    return 


def del_email(user_dict):
    user_input = ""
    while user_input != "0":
        if user_dict["email"] == []:
            print(">>> This contact don`t have email <<<")
            return
        i = 1
        email_text = "\n"
        for email in user_dict["email"]:
            email_text += "".join(f"> {i}) {email}") + "\n"
            i += 1
        print(email_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number email that you want to change: ").strip()
        if user_input == "0":
            return
        chose_email = int(user_input) - 1
        us_email = user_dict["email"][chose_email]
        session.query(EmailDB).filter_by(_property_email=us_email, user_id=user_dict["record"].id).delete()
        session.commit()
        del user_dict["email"][chose_email]
        print("\n>>> Email deleted <<<\n")
    return


def del_adress(user_dict):
    user_input = ""
    while user_input != "0":
        if user_dict["address"] == []:
            print(">>> This contact don`t have address <<<")
            return
        i = 1
        address_text = "\n"
        for address in user_dict["address"]:
            address_text += "".join(f"> {i}) {address}") + "\n"
            i += 1
        print(address_text)
        user_input = input(">>> 0: To enter the contact menu.\n\n<< Chose number address that you want to change: ").strip()
        if user_input == "0":
            return
        chose_address = int(user_input) - 1
        us_address = user_dict["address"][chose_address]
        session.query(AddressDB).filter_by(address=us_address, user_id=user_dict["record"].id).delete()
        session.commit()
        del user_dict["address"][chose_address]
        print("\n>>> Address deleted <<<\n")
    return


def del_birthday(user_dict):
    if user_dict["record"]._birthday_user == None:
        print("\n>>> This contact don`t have birthday date <<<")

    else:
        session.query(RecordBD).filter(RecordBD.id == user_dict["record"].id).\
            update({RecordBD._birthday_user:None}, synchronize_session=False)
        session.commit()
        print("\n>>> Birthday date deleted <<<\n")
        return 

def del_notes(user_dict):
    print(user_dict["note"])
    if user_dict["note"] == []:
        print("\n>>> This contact don`t have birthday date <<<")
    else:
        session.query(NotesDB).filter_by(user_id=user_dict["record"].id).delete()
        session.commit()
        print("\n>>> Birthday date deleted <<<\n")
        return 


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