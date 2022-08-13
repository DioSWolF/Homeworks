from datetime import datetime
import re
from Class import Record, Adress_Book, Name, Phone, Birthday, Iterable


book = Adress_Book()


def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except KeyError or UnboundLocalError :
            print("Write a valid name or command")
            return None

        except ValueError:
            print("This phone number invalid")
            return None

        except IndexError:
            print("Write name and one phone")
            return None

        except AttributeError:
            pass

    return inner


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

        if isinstance(book[rec.name.value].birthday, list):
            book[rec.name.value].birthday = rec.birthday

    else:
        book.add_record(rec)

    return print("Your number has been successfully added.")


@input_error
def change_contact(book, rec: Record) -> None:
    i = 1

    for item in book[rec.name.value].phone:
        print(f"№ {i}: {item}")
        i += 1

    user_len_num = input("Enter № phone: ")
    index_phone = int(user_len_num) - 1

    for i in rec.phone:
        phone = i

    rec.change_phone(book, phone, index_phone)
    return print("Your number has been successfully change.")


@input_error
def delete_contact(book, rec: Record) -> None:
    user_choise = input("What do you want to delete? number/contact : ")

    if user_choise.lower() == "number":
        i = 1

        for item in book[rec.name.value].phone:
            print(f"№ {i}: {item}")
            i += 1     

        user_len_num = input("Enter № phone: ")
        rec.delete_phone(user_len_num)
        return print("Your number has been successfully delete.")

    if user_choise.lower() == "contact":
        del book[rec.name.value]
        return print("Your contact has been successfully delete.")


@input_error
def phone_contact(book, rec: Record) -> None:

    try:
        print(f"{book.get(rec.name.value).name.value}: {book.get(rec.name.value).phone}, Birthday: {book.get(rec.name.value, 'name dont find').birthday.value.date()}, Day to birthday: {days_birthday(book, rec)}")
    
    except AttributeError:
        print(f"{book.get(rec.name.value).name.value}: {book.get(rec.name.value).phone}")

stop_word = ["stop", "exit", "good bye"]


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


def parse_date(user_input):
    date_input = re.findall(r"\d{2}[ /.,\\]\d{2}[ /.,\\]\d{4}", user_input)
   
    if len(date_input) > 0:
        return date_input[-1]
    else:
        return user_input


def show_all(user_input):
    try:
        number_of_records = int(user_input[2])
        Iterable(book.data, number_of_records)

    except IndexError:
        Iterable(book.data)

    for value in book:
        print(value)


def close(*_):
    pass


def main():
    user_input = ""

    while user_input not in stop_word:
        user_input = input("Input command, name and phone: ")
        parse_input = parse_user_input(user_input)

        try:
            command = parse_input[0]
            name = Name(parse_input[1])

            try:
                date = parse_date(parse_input[-1])
                phones = [Phone(ph).value for ph in  parse_input[2:-1]]
                birthday = Birthday(date)
            except re.error:
                phones = [Phone(ph).value for ph in  parse_input[2:]] 
                birthday = None

            rec = Record(name, phones, birthday) 
            func = { 
                "add" : add_contact,
                "change" : change_contact,
                "delete" : delete_contact,                                   
                "phone" : phone_contact
                    }
            command_func = func.get(command, close)
            command_func(book, rec)

        except IndexError or UnboundLocalError:
            pass

        if parse_input[0] == "show" and parse_input[1].lower() == "all":
            show_all(parse_input)

    print("Good bye!")


if __name__ == "__main__":
    main()
