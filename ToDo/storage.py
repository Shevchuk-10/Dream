import json
import os
from typing import List, Dict

FILE_PATH = "todos.json"

def load_todos() -> List[Dict[str, str]]:
    """Завантаження списку завдань із файлу."""
    if not os.path.exists(FILE_PATH):
        return []  # Якщо файл не існує, повертаємо порожній список
    with open(FILE_PATH, "r", encoding="utf-8") as file:  # Вказуємо кодування для відкриття файлу
        return json.load(file)

def save_todos(todos: List[Dict[str, str]]) -> None:
    """Збереження списку завдань у файл."""
    with open(FILE_PATH, "w", encoding="utf-8") as file:  # Вказуємо кодування для запису
        json.dump(todos, file, indent=4)
