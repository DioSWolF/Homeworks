from datetime import datetime
import re
from connect_db import Base
from sqlalchemy import Column, Integer, VARCHAR, Date, ForeignKey, String, Text, null
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from connect_db import session


Base = declarative_base()


class RecordBD(Base):

    __tablename__ = "record_bd"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(250), nullable=False)
    _birthday_user = Column("birthday_date", Date, nullable=True)


    @hybrid_property
    def birthday_user(self):
        return self._birthday_user


    @birthday_user.setter
    def birthday_user(self, value): 
        parse = " .,\/"

        for it in parse:
            value = value.replace(it, ".")

        if value != "":

            try:
                value = datetime.strptime(value ,"%d.%m.%Y")
                self._birthday_user = value

            except ValueError:
                print(  "\n>>> You write invalid date <<<\n"\
                        ">>> Date don`t change <<<")

                self._birthday_user = null


    def create_record(self): 
        if session.query(RecordBD).filter_by(name=self.name).first() == None:
            record = RecordBD(name = self.name)

            session.add(record)
            session.commit()

            return record


    def create_field(self, birthday, bd_rec) -> None:
        self.birthday_user = birthday
        
        if self._birthday_user != null:
            session.query(RecordBD).filter(RecordBD.id == bd_rec.id).\
                update({RecordBD._birthday_user:birthday}, synchronize_session=False)

            session.commit()


class PhoneDB(Base):

    __tablename__ = "phones_bd"

    id = Column(Integer, primary_key=True, autoincrement=True)
    _phone_property = Column("phone", String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("record_bd.id", ondelete="CASCADE"), nullable=False)
    record = relationship("RecordBD")


    @hybrid_property
    def phone_property(self):
        return self._phone_property


    @phone_property.setter
    def phone_property(self, value: str):

        repl_list = """ QWERTYUIOP{}ASDFGHJKL:'ZXCVBNM<>?qwertyuiop[]asdfghjkl;\\'""zxcvbnm,./+-*|()@#$%№&^"""

        for item in repl_list:
            value = value.replace(item, "")

        if len(value) > 7:
            self._phone_property = value
        else:
            print(  "\n>>> You write invalid phone <<<\n"\
                    ">>> Phone don`t change <<<")

            self._phone_property = None


    def create_field(self, phones_user: str, name_id: RecordBD) -> None:
        phones_user = phones_user.split(" ")
        phones_user = list(filter(lambda i: i != "", phones_user))

        for phone in phones_user:
            phones = PhoneDB(phone_property = phone, user_id=name_id.id)

            if session.query(PhoneDB).filter_by(_phone_property=phones._phone_property, user_id = phones.user_id).first() == None and phones._phone_property != None:
                session.add(phones)
            
        session.commit()

    def change_field(self, new_phone, old_phone, name_id):
        self.phone_property = new_phone
        phone_update = session.query(PhoneDB).filter(PhoneDB.user_id == name_id.id, PhoneDB._phone_property == old_phone).\
            update({PhoneDB._phone_property:self._phone_property}, synchronize_session=False)
        # print()
        # session.add(phone_update)
        session.commit()


class NotesDB(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True   )
    note = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("record_bd.id", ondelete="CASCADE"), nullable=False)
    record = relationship("RecordBD")


    def create_field(self, note_text: str, name_id: RecordBD) -> None:

        note_query = session.query(NotesDB).filter(NotesDB.user_id == name_id.id).\
            update({NotesDB.note:note_text}, synchronize_session=False)
        print(len(note_text.replace(" ", "")))
        if note_query == 0 and len(note_text.replace(" ", "")) > 0:
            note = NotesDB(note=note_text, user_id=name_id.id)
            session.add(note)

        session.commit()


class EmailDB(Base):

    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, autoincrement=True   )
    _property_email = Column("email", String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("record_bd.id", ondelete="CASCADE"), nullable=False)
    record = relationship("RecordBD")


    @hybrid_property
    def email_property(self):
        return self._property_email


    @email_property.setter
    def email_property(self, value: str):
        new_value = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", value)

        if len(new_value) >= 1:
            self._property_email = new_value[0]

        else:   
            print(  "\n>>> You write invalid email <<<\n"\
                    ">>> Email don`t change <<<")
            self._property_email = None


    def change_field(self, new_email, old_email, name_id):
        self.email_property = new_email
        phone_update = session.query(EmailDB).filter(EmailDB.user_id == name_id.id, EmailDB._property_email == old_email).\
            update({EmailDB._property_email:self._property_email}, synchronize_session=False)
  
        session.commit()


    def create_field(self, email_list: list, name_id: RecordBD):
        emails_list = email_list.split(" ")
        emails_list = list(filter(lambda i: i != "", emails_list))

        for email in emails_list:
            emails = EmailDB(email_property = email, user_id=name_id.id)

            if session.query(EmailDB).filter_by(_property_email=emails._property_email, user_id=emails.user_id).first() == None and emails._property_email != None:
                session.add(emails)
            
        session.commit()


class AddressDB(Base):

    __tablename__ = "adresses"

    id = Column(Integer, primary_key=True, autoincrement=True   )
    address = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("record_bd.id", ondelete="CASCADE"), nullable=False)
    record = relationship("RecordBD")


    def create_field(self, address_user: str, name_id: RecordBD):

        addresses = AddressDB(address = address_user, user_id=name_id.id)

        if session.query(AddressDB).filter_by(address=addresses.address, user_id=addresses.user_id).first() == None and len(addresses.address.replace(" ", "")) > 0:
            session.add(addresses)
            
        session.commit()


    def change_field(self, new_address, old_address, name_id):
        phone_update = session.query(AddressDB).filter(AddressDB.user_id == name_id.id, AddressDB.address == old_address).\
            update({AddressDB.address : new_address}, synchronize_session=False)
  
        session.commit()