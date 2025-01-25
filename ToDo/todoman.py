from storage import load_todos, save_todos

def show_all_todos():
    todos = load_todos()  # Отримуємо завдання
    if not todos:
        return []  # Якщо завдань немає, повертаємо порожній список
    return todos  # Повертаємо список завдань

def create_todo(title, body):
    todos = load_todos()
    todos.append({"title": title, "body": body, "status": False})
    save_todos(todos)
    print("Задание додано!")

def complete_todo(index):
    todos = load_todos()
    try:
        todos[index - 1]["status"] = True
        save_todos(todos)
        print("Задание отмечено как исполнено!")
    except IndexError:
        print("Задания с таким индексом не существует.")

def delete_todo(index):
    todos = load_todos()
    try:
        deleted = todos.pop(index - 1)
        save_todos(todos)
        print(f"Завдання '{deleted['title']}' видалено!")
    except IndexError:
        print("Задания с таким индексом не существует.")

def edit_todo(index, title, body):
    todos = load_todos()
    try:
        todos[index - 1].update({"title": title, "body": body})
        save_todos(todos)
        print("Задание обновлено!")
    except IndexError:
        print("Задания с таким индексом не существует.")

def show_todo(index):
    todos = load_todos()
    try:
        todo = todos[index - 1]
        status = "✅" if todo["status"] else "❌"
        print(f"{index}. {todo['title']} - {status}\n   {todo['body']}")
    except IndexError:
        print("Задания с таким индексом не существует.")