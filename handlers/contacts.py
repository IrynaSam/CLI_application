from decorators import input_error
from classes.address_book import Record, Name


@input_error
def add_contact(args, book):
    if len(args)<2:
        raise IndexError
    name, phone = args
    if name in book:
        record = book[name]
        record.add_phone(phone)
        return f"Phone added to {name}"
    else:
        record = Record(Name(name))