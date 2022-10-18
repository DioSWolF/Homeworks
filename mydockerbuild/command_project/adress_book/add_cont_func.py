from .сlass import Record, AdressBook, Name, Phone, Birthday, Email, AdressLive, Notes, Iterable
from .show_find_logic import rec_list_print



def add_contact(book:AdressBook):
    name_cont = input("\n>>> 0 to enter the menu.\n\n<< Write contact name: ").strip()

    if name_cont == "0":
        return 

    if name_cont in book:
        return "\n>>> You have a contact with this name! <<<\n"\
               "       >>>Choose another name <<<"
    name_cont = Name(name_cont)
    phone_cont = [Phone("")]
    
    email_cont = [Email("")]
    adress_cont = [AdressLive("")]
    notes_cont = Notes("")
    birthday_cont = Birthday("")
    rec = Record(name_cont, phone_cont, email_cont, adress_cont, notes_cont, birthday_cont)
    del rec.phone[0]
    del rec.email[0]
    del rec.ardess_live[0]

    book.add_record(rec)

    return write_field(book, rec)

def write_field(book:AdressBook, rec: Record):
    user_chose = ""

    while user_chose not in STOP_WORD:
        print(rec_list_print(rec))
        user_chose = input("<< Select the field number to fill in: ").strip()
        user_chose = ADD_FUNC_DICT.get(str(user_chose), error_chose)
        user_chose = user_chose(rec)
        if user_chose != None:
            print(user_chose)
        book.add_record(rec)
        book.save_data()
    return

def write_phone(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write phone number: ").strip()

    if user_input == "0":
        return 
    user_input = user_input.split(" ")
    if rec.phone == []:
        rec.phone.extend([Phone(ph) for ph in user_input])

    else:
        rec.phone.extend([Phone(ph) for ph in user_input])
    rec.phone = list(filter(lambda i: i.value != "", rec.phone))
    return

def write_email(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write email: ").strip()

    if user_input == "0":
        return
    user_input = user_input.split(" ")
    if rec.email == []:
        rec.email.extend(Email(em) for em in user_input)
    else:
        rec.email.extend(Email(em) for em in user_input)
    rec.email = list(filter(lambda i: i.value != "", rec.email))
    return

def write_ardess(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write adress: ").strip()

    if user_input == "0":
        return

    if rec.ardess_live == []:
        rec.ardess_live.extend([AdressLive(user_input)])

    else:
        rec.ardess_live.extend([AdressLive(user_input)])
    rec.ardess_live = list(filter(lambda i: i.value != "", rec.ardess_live))
    return

def write_birthday(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write birthday: ").strip()

    if user_input == "0":
        return
    rec.birthday = Birthday(user_input)
    return

def write_notes(rec: Record) -> None:
    user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write notes: ").strip()

    if user_input == "0":
        return
    rec.notes = Notes(user_input)
    return

def close_bot(*_):
    return "exit"

STOP_WORD = ("stop", "exit", "good bye")

ADD_FUNC_DICT = {   "0" : close_bot,
                    "1" : write_phone, 
                    "2" : write_email,
                    "3" : write_ardess,
                    "4" : write_birthday,
                    "5" : write_notes,
                }

def error_chose(*_):
    return  "\n>>> You chose invalid <<<\n"\
            "     >>>Try again <<<\n"