import pickle
from copy import deepcopy, copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return Person (copy(self.name),
        copy(self.email),
        copy(self.phone),
        copy(self.favorite))
        
        
        
            
            
            
            
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        return Contacts(copy(self.filename), copy(self.contacts) )
        
        

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]

        copy_obj = Contacts(
            deepcopy(self.filename, memo),
            deepcopy(self.contacts, memo)
        )
        memo[id(self)] = copy_obj
        return copy_obj
        
        