from collections import UserDict

class Field():
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass
class Phone(Field):
    pass

        
class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:  
            self.name = name
            if phone is None:
                self.phone = []
            else:
                self.phone = phone

    def add_phone(self, book):
        book[self.name.value].phone.extend(self.phone)

    def change_phone(self, book, phones, index_phone: int()):
        book[self.name.value].phone[index_phone] = phones

    def delete_phone(self, index_phone):
        del book[self.name.value].phone[int(index_phone) - 1]


class AdressBook(UserDict):
    def add_record(self, rec: Record)-> None:
        self.data[rec.name.value] = rec  

    def __str__(self):
        return str(self.data)

book = (AdressBook)