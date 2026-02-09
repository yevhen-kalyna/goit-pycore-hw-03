"""Завдання 2: Генерація набору унікальних випадкових чисел для лотереї."""

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Генерує набір унікальних випадкових чисел для лотерейного білета.

    Args:
        min: Мінімальне можливе число у наборі (не менше 1).
        max: Максимальне можливе число у наборі (не більше 1000).
        quantity: Кількість чисел, які потрібно вибрати.

    Returns:
        Відсортований список унікальних випадкових чисел.
        Порожній список, якщо параметри не відповідають обмеженням.
    """
    if (
        not isinstance(min, int)
        or not isinstance(max, int)
        or not isinstance(quantity, int)
    ):
        return []

    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


if __name__ == "__main__":
    # Приклад використання
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    # Некоректні параметри
    print(get_numbers_ticket(1, 49, 50))  # []
    print(get_numbers_ticket(0, 49, 6))   # []
