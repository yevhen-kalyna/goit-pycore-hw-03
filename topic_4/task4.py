"""Завдання 4: Визначення найближчих днів народження для привітання колег."""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Визначає, кого з колег потрібно привітати з днем народження протягом наступних 7 днів.

    Якщо день народження припадає на вихідний (субота або неділя),
    дата привітання переноситься на наступний понеділок.

    Args:
        users: Список словників з ключами 'name' (str) та 'birthday' (str, формат 'рік.місяць.дата').

    Returns:
        Список словників з ключами 'name' та 'congratulation_date' (формат 'рік.місяць.дата').
    """
    today = datetime.today().date()
    upcoming = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (ValueError, KeyError):
            continue

        # День народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця у днях
        delta_days = (birthday_this_year - today).days

        # Перевіряємо, чи день народження в межах 7 днів
        if delta_days <= 7:
            congratulation_date = birthday_this_year

            # Якщо припадає на суботу — переносимо на понеділок (+2 дні)
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            # Якщо припадає на неділю — переносимо на понеділок (+1 день)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
