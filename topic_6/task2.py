"""Завдання 2: Отримання інформації про котів із текстового файлу."""
import json

def get_cats_info(path: str) -> list[dict[str, str]]:
    """Повертає список словників з інформацією про котів із файлу.

    Формат кожного рядка файлу: "id,name,age".

    Args:
        path: Шлях до текстового файлу з даними про котів.

    Returns:
        Список словників із ключами "id", "name", "age".
        Якщо файл відсутній, пошкоджений або містить некоректні дані,
        функція повертає порожній список.
    """
    cats_info: list[dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                cat_id, name, age = clean_line.split(",")
                cats_info.append({"id": cat_id, "name": name, "age": age})

    except (FileNotFoundError, OSError, ValueError):
        return []

    return cats_info


if __name__ == "__main__":
    # Приклад використання
    cats = get_cats_info("task2.txt")
    print(json.dumps(cats, indent=4))
