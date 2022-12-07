# # from .сlass import AdressBook, Iterable, Record
from mymodel import NotesDB, RecordBD, PhoneDB, EmailDB, AddressDB
from connect_db import session


def find_contact() -> RecordBD:
    user_input = ""

    while True:
        
        user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Enter the text to find contact: ").strip()
        if user_input == "0":
            return "0"

        bd_rec = session.query(RecordBD).filter_by(name=user_input).first()

        if bd_rec == None:
            print("\n>>> Can't find anything <<<\n"\
                    "     >>> Try again <<<")
            continue
        find_contact = "\n"

        rec_list = []

        find_contact += "".join(f"> 1) {bd_rec.name}") + "\n"
        rec_list.append(bd_rec)   

        return bd_rec


def take_user_info(bd_rec: RecordBD) -> dict[str:list[str]] and str:
    birthday_user = ""
    info_phone = session.query(PhoneDB).filter_by(user_id = bd_rec.id).all()
    info_notes = session.query(NotesDB).filter_by(user_id = bd_rec.id).all()
    info_email = session.query(EmailDB).filter_by(user_id = bd_rec.id).all()
    info_address = session.query(AddressDB).filter_by(user_id = bd_rec.id).all()
    birthday_info = session.query(RecordBD).filter_by(id = bd_rec.id).first()

    if birthday_info.birthday_user != None:
        birthday_user = birthday_info.birthday_user

    phone = [i._phone_property for i in list(filter(lambda i: i._phone_property != [], info_phone))]
    phones = ', '.join(phone)

    email = [i._property_email for i in list(filter(lambda i: i._property_email != [], info_email))]
    emails = ', '.join(email)

    adress = [i.address for i in list(filter(lambda i: i.address != [], info_address))]
    adresses = ', '.join(adress)

    note = [i.note for i in list(filter(lambda i: i.note != [], info_notes))]
    notes = ', '.join(note)

    rec_list =  f"\n1) Phones: {phones}", f"2) Email: {emails}", f"3) Adress: {adresses}", \
                    f"4) Birthday date: {birthday_user}", f"5) Notes: {notes}\n\n>>> 0: To enter for the contact menu.\n"

    return_dict = {"record" : bd_rec, "phone":phone, "email" : email, "address":adress, "note":note, "birthday" : birthday_info}

    return return_dict, "\n".join(rec_list)


def show_all():
    records = session.query(RecordBD).all()
    i = 0
    print_text = "\n"
    for rec in records:
        print_text += f"{i}) {rec.name}\n"
        i += 1  
    return print_text


def find_similar():
    while True:
        user_input = input(">>> 0: To exit in main menu.\n<< Write text to find similar: ")
        if user_input == "0":
            return
        print_text = session.query(RecordBD).filter(RecordBD.name.like(f"%{user_input}%")).all()
        i = 0
        text = ""
        for item in print_text:
            text += f"{i}) {item.name}\n"
            i += 1  
        print(text)