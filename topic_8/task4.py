"""Завдання 4: консольний бот-помічник з обробкою помилок через декоратор."""

from collections.abc import Callable
from typing import Any


def input_error(func: Callable[..., str]) -> Callable[..., str]:
    """Декоратор для обробки помилок введення користувача."""

    def inner(*args: Any, **kwargs: Any) -> str:
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."

    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розбирає введений рядок на команду та аргументи."""
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Додає новий контакт."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Змінює телефон існуючого контакту."""
    name, phone = args
    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Повертає телефон контакту за ім'ям."""
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts: dict[str, str]) -> str:
    """Повертає всі контакти у форматі 'ім'я: телефон'."""
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """Точка входу в консольного бота."""
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
