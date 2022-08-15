from collections import UserDict
from datetime import datetime
import pickle
import re


class Field():
    
    def __init__(self, value):
        self.__value = None
        self.value = value


class Birthday(Field):

    @property
    def value(self):
        return self._Field__value


    @value.setter
    def value(self, value): 
        parse = " .,\/"
        for it in parse:
            value = value.replace(it, ".")
        value = datetime.strptime(value ,"%d.%m.%Y")
        self._Field__value = value



class Name(Field):
    pass


class Phone(Field):
    pass
    @property
    def value(self):
        return self._Field__value


    @value.setter
    def value(self, value):
        new_value = re.findall(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}", value)

        if len(value) >= 9 and len(new_value) > 0:
            self._Field__value = value

        
class Record:

    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None) -> None:  
            self.name = name

            if phone is None:
                self.phone = []
            else:
                self.phone = phone

            if birthday is None:
                self.birthday = []
            else:
                self.birthday = birthday


    def add_phone(self, book):
        book[self.name.value].phone.extend(self.phone)


    def change_phone(self, book, phones, index_phone: int()):
        book[self.name.value].phone[index_phone] = phones


    def delete_phone(self, index_phone):
        del book[self.name.value].phone[int(index_phone) - 1]
    

    def days_to_birthday(self, days):
        return days

list_index = 0
number_of_records = 0

class Adress_Book(UserDict):

    def add_record(self, rec: Record)-> None:
        self.data[rec.name.value] = rec
        
    def load_data():
        with open("data.bin", "rb") as file:
            return pickle.load(file)

    def __str__(self):
        return str(self.data)


    def __iter__(self):
        return Iterable(self.data, number_of_records)



class Iterable:

    def __init__(self, data, iter_number_of_records = None):
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
                return f"{data_key[self.start_list_index - 1]}: {', '.join(data_value[self.start_list_index - 1].phone)}. Birthday: {data_value[self.start_list_index - 1].birthday.value.strftime('%d.%m.%Y')}"

            except AttributeError:
                return f"{data_key[self.start_list_index - 1]}: {', '.join(data_value[self.start_list_index - 1].phone)}"


            except IndexError:
                list_index = 0
                raise StopIteration

        list_index = self.start_list_index

        if list_index >= len(self.data):
            list_index = 0

        raise StopIteration


book = Adress_Book