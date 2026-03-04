# Topic 12 — Домашні завдання

У цій папці зібране рішення задачі 1.

## Підготовка середовища

```bash
cd topic_12
python3 -m venv ../.venv
source ../.venv/bin/activate
```

## Задача 1 — `task1.py`

Серіалізація та копіювання об'єктів — адресна книга з pickle.

### Що нового порівняно з Topic 10

- **Серіалізація / десеріалізація** — адресна книга автоматично зберігається у файл `addressbook.pkl` за допомогою модуля `pickle` і відновлюється при наступному запуску програми.
- **`save_data(book)`** — зберігає `AddressBook` у файл.
- **`load_data()`** — завантажує `AddressBook` з файлу або створює нову книгу, якщо файл не знайдено.
- **Збереження при будь-якому виході** — дані зберігаються завжди, незалежно від способу завершення:
  - команди `close` / `exit`;
  - переривання через `Ctrl+C` (`KeyboardInterrupt`);
  - сигнали `SIGTERM` та `SIGHUP` (наприклад, `kill -15`).

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
Enter a command: exit
Good bye!
```

При повторному запуску дані відновлюються:

```text
Welcome to the assistant bot!
Enter a command: all
Contact name: John, phones: 1234567890, birthday: 15.03.1990
Enter a command: exit
Good bye!
```
