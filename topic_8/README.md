# Topic 8 — Домашні завдання

У цій папці зібрані рішення задач 1, 2 та 4.

## Підготовка середовища

```bash
cd topic_8
python3 -m venv ../.venv
source ../.venv/bin/activate
```

## Задача 1 — `task1.py`
Замикання для обчислення чисел Фібоначчі з кешуванням.

Приклад запуску:

```bash
python task1.py
```

Приклад виводу:

```text
55
610
```

Функція:
- `caching_fibonacci() -> Callable[[int], int]`

## Задача 2 — `task2.py`
Генератор дійсних чисел із тексту та підрахунок загального прибутку.

Приклад запуску:

```bash
python task2.py
```

Приклад виводу:

```text
Загальний дохід: 1351.46
```

Функції:
- `generator_numbers(text: str) -> Generator[float, None, None]`
- `sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float`

## Задача 3 — `task3.py`
Файл `task3.py` ще не додано до папки `topic_8`.

## Задача 4 — `task4.py`
CLI-бот для роботи з контактами з обробкою помилок через декоратор `input_error`.

Підтримувані команди:
- `hello`
- `add <name> <phone>`
- `change <name> <phone>`
- `phone <name>`
- `all`
- `close` / `exit`

Приклад запуску:

```bash
python task4.py
```

Приклад сесії:

```text
Welcome to the assistant bot!
Enter a command: add
Enter the argument for the command.
Enter a command: add Bob 0501234356
Contact added.
Enter a command: phone Bob
0501234356
Enter a command: all
Bob: 0501234356
Enter a command: exit
Good bye!
```
