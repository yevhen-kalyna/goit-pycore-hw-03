"""Завдання 1: Обчислення загальної та середньої зарплати розробників з файлу."""


def total_salary(path: str) -> tuple[int, float]:
    """Повертає загальну та середню зарплату розробників із текстового файлу.

    Формат кожного рядка файлу: "Прізвище Ім'я,зарплата" без зайвих роздільників.

    Args:
        path: Шлях до текстового файлу з даними про зарплати.

    Returns:
        Кортеж із двох значень:
        - загальна сума зарплат (int)
        - середня зарплата (float)

        Якщо файл порожній, відсутній або містить некоректні дані,
        функція повертає (0, 0.0).
    """
    total = 0
    developers_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                _, salary = clean_line.split(",")
                total += int(salary)
                developers_count += 1

    except (FileNotFoundError, OSError, ValueError):
        return 0, 0.0

    if developers_count == 0:
        return 0, 0.0

    average = total / developers_count
    return total, average


if __name__ == "__main__":
    # Приклад використання
    total, average = total_salary("task1.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
