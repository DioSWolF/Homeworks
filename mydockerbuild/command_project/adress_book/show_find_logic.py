from .сlass import AdressBook, Iterable, Record


def find_contact(book:AdressBook):
    user_input = ""
    while True:
        user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Enter the text to find contact: ").strip()
        if user_input == "0":
            return "0"
        find_contact = "\n"
        i = 1
        key_list = []
        Iterable(book)
        for _ in book:
            pass

        i = 1
        for value in book:
            key_name, value = value
            if user_input in value:
                iter_text = print_iteration(book, value)
                find_contact += "".join(f"> {i}) {iter_text}") + "\n"
                key_list.append(key_name)
                i += 1
        find_cont = ""
        if find_contact == "\n":
            print("\n>>> Can't find anything <<<\n"\
                    "     >>> Try again <<<")
    
        else:
            print(find_contact)
            find_cont = take_key_rec(book, key_list)
            
        if isinstance(find_cont, Record):
            return find_cont



def take_key_rec(book: AdressBook, key_list: list) -> None:    
    rec = None
    user_input = input(">>> 0: To enter for the contact menu.\n\n<< Chose number contact: ").strip()
    if user_input == "0":
        return "0"
    try:
        rec_key = key_list[int(user_input) - 1]
        rec = book[rec_key]
    except ValueError:
        print("\n>>> Invalid chose <<<")
    except IndexError: 
        print("\n>>> Invalid chose <<<")
        return

    return rec



def find(book:AdressBook):

    find_cont = input("\n>>> 0: To enter the contact menu.\n\n<< Write the text to search in the contact book: ").strip()
    
    while find_cont != "0":
        Iterable(book)
        find_contacts = "\n"
        
        for _ in book:
            pass

        i = 1
        for items in book:
            key_name, value = items
            if find_cont in value:
                iter_text = print_iteration(book, value)
                find_contacts += "".join(f"> {i}) {iter_text}") + "\n"
                i += 1

        if find_contacts == "\n":
            print(  "\n>>> Can't find anything <<<\n"\
                "     >>> Try again <<<")
        else:
            print(find_contacts)

        find_cont = input(">>> 0: To enter the contact menu.\n\n<< Write the text to search in the contact book: ").strip()
    return 

def rec_list_print(rec:Record, change_name: str = None) -> None:
    try:
        birthday = rec.birthday.value.strftime('%d.%m.%Y')
    except AttributeError:
        birthday = ""
    rec.phone = list(filter(lambda i: i.value != "", rec.phone))
    rec.email = list(filter(lambda i: i.value != "", rec.email))
    rec.ardess_live = list(filter(lambda i: i.value != "", rec.ardess_live))
    if change_name == None:
        rec_list =  f"Phones: {', '.join([ph.value for ph in rec.phone])}", f"Email: {', '.join([em.value for em in rec.email])}", f"Adress: {', '.join([adr.value for adr in rec.ardess_live])}", \
                    f"Birthday date: {birthday}", f"Notes: {rec.notes.value}"
    else:
        rec_list =  f"Name: {change_name.value}", f"Phones: {', '.join([ph.value for ph in rec.phone])}", f"Email: {', '.join([em.value for em in rec.email])}", f"Adress: {', '.join([adr.value for adr in rec.ardess_live])}", \
                    f"Birthday date: {birthday}", f"Notes: {rec.notes.value}" 
    
    list_text = f"\nContact name: {rec.name.value}\nChange field:\n"      

    i = 1
    for items in rec_list:
        list_text += f"> {i}) {items}\n"
        i += 1

    list_text += f"\n>>> 0: Exit to main menu\n"

    return list_text

def show_all(book:AdressBook):
    Iterable(book)
    print_cont = ""
    
    for _ in book:
        pass

    i = 1 
    for items in book:
        key_name, value = items
        iter_text = print_iteration(book, value)
        print_cont += "".join(f"> {i}) {iter_text}") + "\n"
        i += 1

    return print_cont

def print_iteration(book:AdressBook, value):
    value = value.split("/||")
    name, phones, email, adress, birthday, notes = value
    print_str = ""
    print_str = f"Name {name}, Phones: {phones}; Email: {email}; Adress: {adress}; Birthday date: {birthday}; Notes: {notes};"
    return print_str

def show(book:AdressBook):


    user_end_index = input("\n>>> 0: To enter the contact menu.\n\n<< How many contacts do you want to show: ").strip()
    
    
    i = 1

    while user_end_index != 0:
        
        print_cont = "\n"
        try:
            user_end_index = int(user_end_index)
        except ValueError:
            print("\n>>> You write text, need number! <<<")
            return
        if user_end_index > len(book):
            i = 1
            show_all(book)
        Iterable(book, user_end_index)
        if len(book) < i:
            i = 1
        for items in book:
            key_name, value = items
            iter_text = print_iteration(book, value)
            print_cont += "".join(f"> {i}) {iter_text}") + "\n"
            i += 1

        print(print_cont)
        try:
            user_end_index = int(input(">>> 0: To enter the contact menu.\n\n<< How many contacts do you want to show: ").strip())
        except ValueError:
            print("\n>>> Invalid chose <<<")
        if user_end_index == 0:
            return 

    Iterable(book)
    for _ in book:
        pass

    return
