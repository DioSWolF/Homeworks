from datetime import datetime
import pickle
import re
from Class import Record, Adress_Book, Name, Phone, Birthday, Iterable


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            save_data(book)
            with open("data.bin", "rb") as file:
                return pickle.load(file)
        except UnboundLocalError:
            return "Write or change valid phone"
        except KeyError:
            return "Write a valid name or command"
        except ValueError:
            return "This phone number invalid"
        except IndexError:
            return "Write name and one phone"
        except AttributeError:
            pass
    return inner


def save_data(book):
    with open("data.bin", "wb") as file:
        pickle.dump(book, file)


@input_error
def load_data():
    with open("data.bin", "rb") as file:
        return pickle.load(file)


@input_error
def add_contact(book, rec: Record) -> None:
    new_list = []
    for value in filter(lambda x: x != None, rec.phone):
        new_list.append(value)
    rec.phone = new_list
    if rec.name.value in book.keys():
        for i in rec.phone:
            if i not in book[rec.name.value].phone:
                rec.add_phone(book)
    
        book[rec.name.value].birthday = rec.birthday        
    else:
        book.add_record(rec)
    return "Your number has been successfully added."


@input_error
def change_contact(book, rec: Record) -> None:
    i = 1
    new_list = []
    if len(book[rec.name.value].phone) > 0:
        for item in book[rec.name.value].phone:
            print(f"№ {i}: {item}")
            i += 1
    else:
        return "This contact don`t have phone"
    user_len_num = input("Enter № phone: ")
    index_phone = int(user_len_num) - 1
    for value in filter(lambda x: x != None, rec.phone):
        new_list.append(value)
    for i in new_list:
        phone = i
    rec.change_phone(book, phone, index_phone)
    return "Your number has been successfully change."


@input_error
def delete_contact(book, rec: Record) -> None:
    user_choise = input("What do you want to delete? number/contact : ")
    if user_choise.lower() == "number":
        i = 1
        for item in book[rec.name.value].phone:
            print(f"№ {i}: {item}")
            i += 1     
        user_len_num = input("Enter № phone: ")
        rec.delete_phone(user_len_num, book)
        return "Your number has been successfully delete."
    if user_choise.lower() == "contact":
        del book[rec.name.value]
        return "Your contact has been successfully delete."


@input_error
def phone_contact(book, rec: Record) -> None:
    try:
        return f"\n{book.get(rec.name.value).name.value}: {', '.join(book[rec.name.value].phone)}. "\
               f"Birthday: {book.get(rec.name.value, 'name dont find').birthday.value.date()}, "\
               f"Day to birthday: {days_birthday(book, rec)}\n"
    except AttributeError:
        return f"\n{book.get(rec.name.value).name.value}: {', '.join(book[rec.name.value].phone)}\n"


def days_birthday(book, rec: Record):
    now_date = datetime.now()
    date_birthday = datetime(year = now_date.year, month = book[rec.name.value].birthday.value.month, day = book[rec.name.value].birthday.value.day)
    days_birth = date_birthday - now_date
    return rec.days_to_birthday(days_birth.days)


@input_error
def parse_user_input(user_input):
    user_input = user_input.strip()
    user_input = user_input.split(" ")
    new_user_input = []
    for i in filter(lambda x: len(x) >= 1, user_input):
        new_user_input.append(i)
    new_user_input[0] = new_user_input[0].lower()
    return new_user_input


@input_error
def parse_date(user_input):
    date_input = re.findall(r"\d{2}[ /.,\\]\d{2}[ /.,\\]\d{4}", user_input)
    if len(date_input) > 0:
        return date_input[-1] 
    else:
        return user_input


def show_all(_):
    all_contacts = "\n"
    Iterable(book)
    for value in book:
        all_contacts += "".join(value) + "\n"
    return all_contacts


def show(book, num_cont):
    number_of_records = int(num_cont.name.value)
    Iterable(book, number_of_records)
    all_contacts = "\n"
    for value in book:
        all_contacts += "".join(value) + "\n"
    return all_contacts


def close(*_):
    pass


def find(book, rec: Record):  
    Iterable(book)
    find_contacts = "\n"
    for value in book:
        if rec.name.value in value:
            find_contacts += "".join(value) + "\n"
    return find_contacts


def main():
    user_input = ""
    while user_input not in STOP_WORD:
        user_input = input("Input command, name and phone: ")
        parse_input = parse_user_input(user_input)
        if parse_input[0] == "show" and parse_input[1].lower() == "all":
            print(show_all(parse_input))
            continue
        try:
            command = parse_input[0]
            name = Name(parse_input[1])
            try:
                date = parse_date(parse_input[-1])
                phones = [Phone(ph).value for ph in  parse_input[2:-1]]
                birthday = Birthday(date)
            except ValueError:
                phones = [Phone(ph).value for ph in  parse_input[2:]] 
                birthday = []
            rec = Record(name, phones, birthday) 
            command_func = FUNC.get(command, close)
            print_return_command = command_func(book, rec)
        except IndexError or UnboundLocalError:
            print_return_command = None
        if not print_return_command == None:
            print(print_return_command)
    print("Good bye!")
    save_data(book)


STOP_WORD = ("stop", "exit", "good bye")
FUNC = { 
                "add" : add_contact,                    # add {name} *{phones} {birthday}
                "change" : change_contact,              # change {name} {phone}
                "delete" : delete_contact,              # delete {name}                   
                "phone" : phone_contact,                # phone {name}
                "find" : find,                          # find {text}
                "show" : show                           # show {number}
        }                                               # show all


if __name__ == "__main__":
    book = Adress_Book()
    book = load_data()
    main()