"""Завдання 3: Візуалізація структури директорії у вигляді tree з кольорами."""

import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_directory_tree(directory: Path, prefix: str = "") -> None:
    """Рекурсивно виводить структуру директорії у форматі tree.

    Args:
        directory: Шлях до директорії, яку потрібно вивести.
        prefix: Поточний префікс відступу для побудови дерева.
    """
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )
    except PermissionError:
        print(f"{prefix}{Fore.RED}└── [Немає доступу]{Style.RESET_ALL}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        if entry.is_dir():
            print(f"{prefix}{branch}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
            print_directory_tree(entry, next_prefix)
        else:
            print(f"{prefix}{branch}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main() -> None:
    """Запускає CLI-скрипт для виведення структури директорії."""
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Використання: python task3.py /шлях/до/директорії")
        return

    directory_path = Path(sys.argv[1]).expanduser().resolve()

    if not directory_path.exists():
        print(f"Помилка: шлях '{directory_path}' не існує.")
        return

    if not directory_path.is_dir():
        print(f"Помилка: шлях '{directory_path}' не є директорією.")
        return

    print(f"{Fore.BLUE}{directory_path.name}{Style.RESET_ALL}")
    print_directory_tree(directory_path)


if __name__ == "__main__":
    main()
