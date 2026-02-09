"""Завдання 1: Розрахунок кількості днів між заданою датою і поточною."""

from datetime import datetime


def get_days_from_today(date: str) -> int:
    """Розраховує кількість днів між заданою датою і поточною датою.

    Args:
        date: Рядок з датою у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').

    Returns:
        Ціле число — кількість днів від заданої дати до поточної.
        Додатне значення, якщо задана дата в минулому; від'ємне — якщо в майбутньому.

    Raises:
        ValueError: Якщо формат дати некоректний.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError) as e:
        raise ValueError(f"Некоректний формат дати: '{date}'. Очікується 'РРРР-ММ-ДД'.") from e

    today = datetime.today().date()
    delta = today - target_date

    return delta.days


if __name__ == "__main__":
    # Приклади використання
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2025-02-09"))

    # Некоректний формат
    try:
        print(get_days_from_today("09-10-2021"))
    except ValueError as e:
        print(e)
