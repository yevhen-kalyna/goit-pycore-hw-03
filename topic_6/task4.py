"""Завдання 4: Консольний бот-помічник для роботи з контактами."""


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розбирає введений рядок на команду та аргументи.

    Команда розпізнається незалежно від регістру.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Додає новий контакт у словник."""
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Змінює номер телефону існуючого контакту."""
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Повертає номер телефону за ім'ям контакту."""
    if len(args) != 1:
        return "Invalid command."

    name = args[0]
    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    """Повертає всі збережені контакти у вигляді рядка."""
    if not contacts:
        return "No contacts saved."

    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main() -> None:
    """Запускає цикл запит-відповідь для взаємодії з користувачем."""
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
