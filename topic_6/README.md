# Topic 6 — Домашні завдання

У цій папці зібрані рішення задач 1–4.

## Підготовка середовища

```bash
cd topic_6
python3 -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt
```

## Задача 1 — `task1.py`
Обчислення загальної та середньої зарплати з файлу.

Приклад запуску:

```bash
python task1.py
```

Приклад виводу:

```text
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000.0
```

Функція:
- `total_salary(path: str) -> tuple[int, float]`

## Задача 2 — `task2.py`
Читання інформації про котів з файлу у список словників.

Приклад запуску:

```bash
python task2.py
```

Приклад виводу:

```text
[
	{
		"id": "60b90c1c13067a15887e1ae1",
		"name": "Tayson",
		"age": "3"
	},
	{
		"id": "60b90c2413067a15887e1ae2",
		"name": "Vika",
		"age": "1"
	},
	{
		"id": "60b90c2e13067a15887e1ae3",
		"name": "Barsik",
		"age": "2"
	},
	{
		"id": "60b90c3b13067a15887e1ae4",
		"name": "Simon",
		"age": "12"
	},
	{
		"id": "60b90c4613067a15887e1ae5",
		"name": "Tessi",
		"age": "5"
	}
]
```

Функція:
- `get_cats_info(path: str) -> list[dict[str, str]]`

## Задача 3 — `task3.py`
Виведення структури директорії у форматі `tree` з кольорами через `colorama`.

Приклад запуску:

```bash
python task3.py /абсолютний/або/відносний/шлях/до/директорії
```

Приклад виводу (для поточної папки `topic_6`):

```text
topic_6
├── README.md
├── requirements.txt
├── task1.py
├── task1.txt
├── task2.py
├── task2.txt
├── task3.py
├── task4.py
├── TASK_1.md
├── TASK_2.md
├── TASK_3.md
└── TASK_4.md
```

## Задача 4 — `task4.py`
CLI-бот для роботи з контактами.

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
Enter a command: How can I help you?
Enter a command: Contact added.
Enter a command: 1234567890
Enter a command: Contact updated.
Enter a command: John: 0987654321
Enter a command: Good bye!
```
