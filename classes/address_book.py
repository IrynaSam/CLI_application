from collections import UserDict

class Field: # зберігає одне значення 
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if phone 
        
        

class Record: # зберігає всю картку з даними користувача( ім'я, телефон, дату народження і.т.д)
    def __init__(self, name):
        self.name = name
        self.phones = []
        
    def add_phone(self, phone):
        pass
    
    def remove_phone(self, phone):
        pass
    
    def edit_phone(self, phone):
        pass

class AddressBook(UserDict): # усі контакти (усі Record)
    def add_record(self, record):
        self.data[record.name.value] = record
        
            