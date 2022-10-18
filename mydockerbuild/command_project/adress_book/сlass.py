from collections import UserDict
from datetime import datetime
import pickle
import re


class Field:
    def __init__(self, value):
        self.__value = ""
        self.value = value


class Name(Field):
    pass
class AdressLive(Field):
    pass
class Notes(Field):
    pass
class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value): 
        repl_list = """ QWERTYUIOP{}ASDFGHJKL:'ZXCVBNM<>?qwertyuiop[]asdfghjkl;\\'""zxcvbnm,./+-*|()@#$%№&^"""
        for item in repl_list:
            value = value.replace(item, "")
        if len(value) > 7:
            self.__value = value
        else:
            print(  "\n>>> You write invalid phone <<<\n"\
                    ">>> Phone don`t change <<<")
            self.__value = ""

class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value): 
        new_value = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", value)
        if len(new_value) >= 1:
            self.__value = new_value[0]
        else:   
            print(  "\n>>> You write invalid email <<<\n"\
                    ">>> Email don`t change <<<")
            self.__value = ""


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value): 
        parse = " .,\/"
        for it in parse:
            value = value.replace(it, ".")
        if value != "":
            try:
                value = datetime.strptime(value ,"%d.%m.%Y")
            except ValueError:
                print(  "\n>>> You write invalid date <<<\n"\
                        ">>> Date don`t change <<<")
                self.__value = ""
        self.__value = value




class Record:
    def __init__(self, name: Name, phone: Phone = None, email: Email = None, ardess_live: AdressLive = None, birthday: Birthday = None, notes: Notes = None) -> None:  
            self.name = name
            self.notes = notes
            
            if phone == None:
                self.phone = []
            else:
                self.phone = phone

            if email == None:
                self.email = []
            else:
                self.email = email

            if phone == None:
                self.ardess_live = []
            else:
                self.ardess_live = ardess_live

            if birthday == None:
                self.birthday = ""
            else:
                self.birthday = birthday
            

class AdressBook(UserDict):

    def add_record(self, rec: Record)-> None:
        self.data[rec.name.value] = rec


    def __iter__(self):
        return Iterable(self.data, number_of_records)
    
    def save_data(self):
        with open("book_data.bin", "wb") as file:
            pickle.dump(self.data, file)

    def load_data(self):
        try:
            with open("book_data.bin", "rb") as file:
                self.data = pickle.load(file)
                return self.data 
        except FileNotFoundError:
            with open("book_data.bin", "wb") as file:
                pickle.dump("", file)
            with open("book_data.bin", "rb") as file:
                return 

list_index = 0
number_of_records = 0


class Iterable:
    def __init__(self, data: AdressBook, iter_number_of_records = None):
        global number_of_records
        self.current_index = 0
        self.data = data
        self.start_list_index = list_index
        if iter_number_of_records == None:
            number_of_records = len(self.data)
        else:
            number_of_records = iter_number_of_records
        self.iter_number_of_records = number_of_records

        
    def __next__(self):
        global list_index
        if self.current_index <  self.iter_number_of_records:
            self.current_index += 1
            self.start_list_index += 1
            data_key = list(self.data.keys())
            data_value = list(self.data.values())
            try:
                try:
                    birthday = data_value[self.start_list_index - 1].birthday.value.strftime('%d.%m.%Y')
                except AttributeError:
                    birthday = ""
                phone = data_value[self.start_list_index - 1].phone
                email = data_value[self.start_list_index - 1].email
                adress = data_value[self.start_list_index - 1].ardess_live
            except IndexError:
                number_of_records = len(self.data)
            try:    
                return data_key[self.start_list_index  - 1], f"{data_key[self.start_list_index  - 1]}/||{', '.join([i.value for i in phone])}/||{', '.join([i.value for i in email])}/||"\
                    f"{', '.join([i.value for i in adress])}/||{birthday}/||{data_value[self.start_list_index  - 1].notes.value}"
            except IndexError:
                list_index = 0
                raise StopIteration
        list_index = self.start_list_index
        if list_index >= len(self.data):
            list_index = 0
        raise StopIteration

# f"Name {data_key[self.start_list_index - 1]}, Phones: {', '.join([i.value for i in phone])}; Email: {', '.join([i.value for i in email])}; "\
# f"Adress: {', '.join([i.value for i in adress])}; Birthday date: {data_value[self.start_list_index - 1].birthday.value}; Notes: {data_value[self.start_list_index - 1].notes.value};"