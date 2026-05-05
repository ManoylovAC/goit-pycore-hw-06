from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError('Name must be a non-empty string.')
        super().__init__(value)
        self.value = value


class Phone(Field):
    def __init__(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Phone number must be 10 digits.')
        super().__init__(value)
        self.value = value


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        for p in self.phones:
            if p.value == old_phone:
                p = Phone(new_phone)

    def find_phone(self, phone: str):
        finded_phones = [p for p in self.phones if p.value == phone]
        return finded_phones[0].value if finded_phones else None

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        return f'Contact name: {self.name.value}, phones: {phones}'


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]


if __name__ == '__main__':
    try:
        # Створення адресної книги
        book = AddressBook()

        # Створення запису для John
        john_record = Record('John')
        john_record.add_phone('1234567890')
        john_record.add_phone('5555555555')

        # Додавання запису John до адресної книги
        book.add_record(john_record)

        # Створення та додавання нового запису для Jane
        jane_record = Record('Jane')
        jane_record.add_phone('9876543210')
        book.add_record(jane_record)

        # Виведення всіх записів у книзі
        for name, record in book.data.items():
            print(record)

        # Знаходження та редагування телефону для John
        john = book.find('John')
        john.edit_phone('1234567890', '_1112223333')
        # john.edit_phone('1234567890', '11122RT333')

        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

        # Пошук конкретного телефону в записі John
        found_phone = john.find_phone('5555555555')
        print(f'{john.name}: {found_phone}')  # Виведення: 5555555555

        # Видалення запису Jane
        book.delete('Jane')
    # Виведення помилок
    except Exception as e:
        print(f'! Виникла помилка. Перевірте вхідні дані: {e}')
