import re

phone_list = {}
stop_words = ["good bye", "close", "exit"]


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Write a valid name or command")
            return None
        except ValueError:
            print("This phone number invalid")
            return None
        except IndexError:
            print("Write name and one phone")
            return None
    return inner


@input_error
def print_hello(_):
    return "Hello! How can I help you?"

def valid_number(phone):
    result = re.findall(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}", phone)
    if len(result) <= 0:
        raise ValueError
    return result

def valid_username(username):
    if username[0] == "change":
        if username[1] not in phone_list:
            raise KeyError
    if username[0] == "add":
        if username[1] in phone_list:
            raise KeyError
    return 


@input_error
def add_phone(info_phone):
    if len(info_phone) > 3:
        raise IndexError
    global phone_list
    valid_username(info_phone)
    username = info_phone[1]
    phone = info_phone[2]
    phone_list.update({username : phone})
    return "Your number has been successfully added."


@input_error
def change_phone(info_phone):
    if len(info_phone) > 3:
        raise IndexError
    global phone_list
    valid_username(info_phone)
    username = info_phone[1]
    phone = info_phone[2]
    phone_list.update({username : phone})
    return "Your number has been successfully changed."


@input_error
def phone_show(info_phone):
    if len(info_phone) > 2:
        raise KeyError
    username = info_phone[1]
    phone = phone_list[username]
    return "".join(f"{username}: {phone}")
    

@input_error
def show_all_phone(_):
    new_list = ""
    for username, phone in phone_list.items():
        new_list += ("".join(f"{username}: {phone}\n"))
    return new_list


func = {
        "hello" : print_hello,
        "add" : add_phone,
        "change" : change_phone,
        "phone" : phone_show,
        "show all" : show_all_phone
        }


@input_error
def parse_user_imput(user_command):
    command = user_command.split(" ")
    if command[0].lower() == "show" and command[1].lower() == "all":
        func_key = func.get("show all")
        user_command_parse = func_key(command)
        return user_command_parse
    func_key = func.get(command[0].lower(), close)
    user_command_parse = func_key(command)
    return user_command_parse


def close(user_command):
        pass 

def main():
    user_command = ""
    while user_command not in stop_words:
        user_command = input("Input your command(hello, add, change, phone, show all): ")
        parse_user_command = user_command.strip()
        func_user = parse_user_imput(parse_user_command)
        if func_user is not None:
            print(func_user)
    print("Good bye!")
main()

