# Topic 9 — Домашні завдання

У цій папці зібране рішення задачі 1.

## Підготовка середовища

```bash
cd topic_9
python3 -m venv ../.venv
source ../.venv/bin/activate
```

## Задача 1 — `task1.py`
Реалізація системи керування адресною книгою з використанням ООП.

### Реалізовані сутності
- `Field` — базовий клас для полів запису.
- `Name` — клас для імені контакту (обов’язкове поле).
- `Phone` — клас для номера телефону з валідацією (рівно 10 цифр).
- `Record` — контакт (ім’я + список телефонів).
- `AddressBook` — колекція контактів із методами керування.

### Реалізована функціональність
- `AddressBook.add_record(record)` — додає запис.
- `AddressBook.find(name)` — шукає запис за ім’ям.
- `AddressBook.delete(name)` — видаляє запис за ім’ям.
- `Record.add_phone(phone)` — додає телефон.
- `Record.remove_phone(phone)` — видаляє телефон.
- `Record.edit_phone(old_phone, new_phone)` — редагує телефон.
- `Record.find_phone(phone)` — шукає телефон у записі.

## Приклад запуску

```bash
python task1.py
```

## Приклад виводу

```text
Contact name: John, phones: 1234567890; 5555555555
Contact name: Jane, phones: 9876543210
Contact name: John, phones: 1112223333; 5555555555
John: 5555555555
```
