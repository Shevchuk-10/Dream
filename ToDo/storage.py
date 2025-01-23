import json
import os

FILE_PATH = "todos.json"

def load_todos():
    """Завантаження списоку завдань із файлу."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_todos(todos):
    """Збереження списоку завдань у файл."""
    with open(FILE_PATH, "w") as file:
        json.dump(todos, file, indent=4)