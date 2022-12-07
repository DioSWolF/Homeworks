from mymodel import NotesDB, RecordBD, PhoneDB, EmailDB, AddressDB
from .show_find_logic import take_user_info
from connect_db import session


def add_contact() -> None:
    name_cont = input("\n>>> 0 to enter the menu.\n\n<< Write contact name: ").strip()

    if name_cont == "0" or name_cont == "":
        return 

    bd_rec = RecordBD(name=name_cont)
    bd_rec = bd_rec.create_record()

    if bd_rec == None:
        return "\n>>> You have a contact with this name! <<<\n"\
               "       >>>Choose another name <<<"

    return write_field(bd_rec)
# # print(rec_list_print(rec))


def write_field(bd_rec:RecordBD) -> None:
    user_chose = ""
    bd_rec = session.query(RecordBD).filter_by(name=bd_rec.name).first()
    
    while True:
        _, rec_list = take_user_info(bd_rec)
        print(rec_list)

        user_chose = input("<< Select the field number to fill in: ").strip()
        print(user_chose)
        if user_chose == "0":
            break

        user_func = ADD_FUNC_DICT.get(str(user_chose), error_chose)

        try:
            user_input = input(FRASES_LIST[user_chose])

        except KeyError:
            print("\n>>> You chose invalid <<<\n"\
            "     >>>Try again <<<\n")
            continue 

        user_func = user_func(user_input, bd_rec)

        if user_func != None:
            print(user_func)

    return


def close_bot(*_) -> str:
    return "exit"


STOP_WORD = ("stop", "exit", "good bye")

ADD_FUNC_DICT = {   "0" : close_bot,
                    "1" : PhoneDB().create_field, 
                    "2" : EmailDB().create_field,
                    "3" : AddressDB().create_field,
                    "4" : RecordBD().create_field,
                    "5" : NotesDB().create_field,
                }

FRASES_LIST = {
                "1" : "\n>>> 0: To enter the contact menu.\n\n<< Write phone number: ",
                "2" : "\n>>> 0: To enter the contact menu.\n\n<< Write email: ",
                "3" : "\n>>> 0: To enter the contact menu.\n\n<< Write adress: ",
                "4" : "\n>>> 0: To enter the contact menu.\n\n<< Write birthday: ",
                "5" : "\n>>> 0: To enter the contact menu.\n\n<< Write notes: ",
}
def error_chose(*_):
    return  "\n>>> You chose invalid <<<\n"\
            "     >>>Try again <<<\n"