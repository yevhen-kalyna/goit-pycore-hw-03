# Topic 10 — Домашні завдання

У цій папці зібране рішення задачі 1.

## Підготовка середовища

```bash
cd topic_10
python3 -m venv ../.venv
source ../.venv/bin/activate
```

## Задача 1 — `task1.py`
Розширена ООП адресна книга з CLI-ботом: додано підтримку днів народження та інтерактивний інтерфейс командного рядка.

### Реалізовані сутності
- `Field` — базовий клас для полів запису.
- `Name` — клас для імені контакту (обов'язкове поле).
- `Phone` — клас для номера телефону з валідацією (рівно 10 цифр).
- `Birthday` — клас для дня народження з валідацією формату DD.MM.YYYY.
- `Record` — контакт (ім'я + список телефонів + день народження).
- `AddressBook` — колекція контактів із методами керування та пошуком найближчих днів народження.

### Підтримувані команди
- `add [ім'я] [телефон]` — додати контакт або телефон до існуючого контакту.
- `change [ім'я] [старий телефон] [новий телефон]` — змінити телефонний номер.
- `phone [ім'я]` — показати телефонні номери контакту.
- `all` — показати всі контакти.
- `add-birthday [ім'я] [DD.MM.YYYY]` — додати дату народження.
- `show-birthday [ім'я]` — показати дату народження.
- `birthdays` — показати дні народження протягом наступного тижня.
- `hello` — отримати вітання від бота.
- `close` / `exit` — закрити програму.

## Приклад запуску

```bash
python task1.py
```

## Приклад виводу

```text
Welcome to the assistant bot!
Enter a command: add John 1234567890
Contact added.
Enter a command: add-birthday John 15.03.1990
Birthday added.
Enter a command: show-birthday John
15.03.1990
Enter a command: phone John
1234567890
Enter a command: all
Contact name: John, phones: 1234567890, birthday: 15.03.1990
Enter a command: birthdays
No upcoming birthdays.
Enter a command: exit
Good bye!
```
