"""Завдання 1: ООП-модель адресної книги."""

from collections import UserDict


class Field:
    """Базовий клас для полів запису."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту."""


class Phone(Field):
    """Клас для зберігання номера телефону з валідацією."""

    def __init__(self, value: str) -> None:
        if not self._is_valid_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

    @staticmethod
    def _is_valid_phone(value: str) -> bool:
        return len(value) == 10 and value.isdigit()


class Record:
    """Клас для зберігання даних одного контакту."""

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)
        if phone_obj is None:
            raise ValueError(f"Phone {phone} not found.")
        self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_obj = self.find_phone(old_phone)
        if phone_obj is None:
            raise ValueError(f"Phone {old_phone} not found.")

        self.phones[self.phones.index(phone_obj)] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Клас для зберігання та керування записами контактів."""

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for _, record in book.data.items():
        print(record)

    john = book.find("John")
    if john is not None:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")

    book.delete("Jane")