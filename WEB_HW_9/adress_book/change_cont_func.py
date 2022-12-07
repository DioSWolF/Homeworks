# from .сlass import Name, Phone, Birthday, Email, AdressLive, Notes, Record
# # from .add_cont_func import write_ardess, write_email, write_phone
from .show_find_logic import find_contact, take_user_info
from mymodel import NotesDB, RecordBD, PhoneDB, EmailDB, AddressDB
from connect_db import session


def change_contact() -> None:
    rec_find = ""
    while rec_find not in STOP_WORD:
        rec_find = find_contact()

        if rec_find == "0":
            return
    
        if isinstance(rec_find, RecordBD):
            return take_contact(rec_find)


def take_contact(bd_rec: RecordBD) -> None:
    user_chose = ""

    bd_rec = session.query(RecordBD).filter_by(name=bd_rec.name).first()

    while user_chose not in STOP_WORD:
        info_dict, rec_list = take_user_info(bd_rec)
        print(rec_list)

        user_input = input(f"\n<< Select the field number to change it: ").strip()
        user_chose = CHANGE_FUNC_DICT.get(str(user_input), error_chose)

        if user_input == "0":
            return
        try:
            user_input = input(FRASES_LIST[user_input])

        except KeyError:
            print("\n>>> You chose invalid <<<\n"\
            "     >>>Try again <<<\n")
            continue

        user_chose = user_chose(user_input, info_dict)

        if user_chose != None:
            user_chose
    return


def change_birthday(user_input: str, info_dict: dict[str:list[str]]) -> None:
    RecordBD().create_field(user_input, info_dict["record"])


def change_notes(user_input: str, info_dict: dict[str:list[str]]) -> None:
    NotesDB().create_field(user_input, info_dict["record"])


def change_phone(phone_num: str, info_dict: dict[str:list[str]]) -> None:
    if len(info_dict["phone"]) == 0:
        PhoneDB().create_field(phone_num, info_dict["record"])

    else:
        while True:

            i = 1
            phone_list = []

            for phone in info_dict["phone"]:
                phone_list.append(f"{i}) {phone}")
                i += 1

            phone_print = f"\n".join(phone_list)

            print(f"\nPhones: \n{phone_print}\n\n>>> 0: To enter for the contact menu.\n>>> +: To add new phone.\n")
            user_input = input("<< Write № phone, what you need change: ")

            if user_input == "0":
                return

            if user_input == "+":
                PhoneDB().create_field(phone_num, info_dict["record"])
                return

            try:
                PhoneDB().change_field(phone_num, info_dict["phone"][int(user_input) - 1], info_dict["record"])
                return
            except IndexError:
                pass


def change_email(new_email: str, info_dict: dict[str:list[str]]) -> None:
    if len(info_dict["email"]) == 0:
        EmailDB().create_field(new_email, info_dict["record"])

    else:
        while True:

            i = 1
            email_list = []

            for email in info_dict["email"]:
                email_list.append(f"{i}) {email}")
                i += 1

            email_list = f"\n".join(email_list)

            print(f"\nEmails: \n{email_list}\n\n>>> 0: To enter for the contact menu.\n>>> +: To add new email.\n")
            user_input = input("<< Write № phone, what you need change: ")

            if user_input == "0":
                return

            if user_input == "+":
                EmailDB().create_field(new_email, info_dict["record"])
                return

            try:
                EmailDB().change_field(new_email, info_dict["email"][int(user_input) - 1], info_dict["record"])
                return
            except IndexError:
                pass


def change_address(new_address: str, info_dict: dict[str:list[str]]) -> None:

    if len(info_dict["address"]) == 0:
        AddressDB().create_field(new_address, info_dict["record"])

    else:
        while True:

            i = 1
            address_list = []

            for address in info_dict["address"]:
                address_list.append(f"{i}) {address}")
                i += 1

            address_list = f"\n".join(address_list)

            print(f"\nEmails: \n{address_list}\n\n>>> 0: To enter for the contact menu.\n>>> +: To add new address.\n")
            user_input = input("<< Write № phone, what you need change: ")

            if user_input == "0":
                return

            if user_input == "+":
                AddressDB().create_field(new_address, info_dict["record"])
                return

            try:
                EmailDB().change_field(new_address, info_dict["address"][int(user_input) - 1], info_dict["record"])
                return
            except IndexError:
                pass


def error_chose(*_):
    return  "\n>>> You chose invalid <<<"\
            "      >>>Try again <<<\n"


def close_bot(*_):
    return "exit"


CHANGE_FUNC_DICT = {
                    "0" : close_bot,                # ready
                    "1" : change_phone,              # ready
                    "2" : change_email,              #
                    "3" : change_address,             #
                    "4" : change_birthday,            #
                    "5" : change_notes,          # ready
                    }


FRASES_LIST = {
                "1" : "\n>>> 0: To enter the contact menu.\n\n<< Write new phone number: ",
                "2" : "\n>>> 0: To enter the contact menu.\n\n<< Write new email: ",
                "3" : "\n>>> 0: To enter the contact menu.\n\n<< Write new adress: ",
                "4" : "\n>>> 0: To enter the contact menu.\n\n<< Write new birthday: ",
                "5" : "\n>>> 0: To enter the contact menu.\n\n<< Write new notes: ",
                }
  

STOP_WORD = ("0","stop", "exit", "good bye")
                    # "2" : add_phone,