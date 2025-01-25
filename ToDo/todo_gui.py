import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Імпортуємо PIL для роботи з іконками
from todoman import show_all_todos, create_todo, complete_todo, delete_todo, edit_todo

# Змінна для збереження стану опису
task_descriptions = {}

def refresh_todos():
    todos_list.delete(0, tk.END)
    todos = show_all_todos()
    for index, todo in enumerate(todos, start=1):
        status = "✔️" if todo["status"] else "❌"
        todos_list.insert(tk.END, f"{index}. {todo['title']} - {status}")
        # Спочатку приховуємо опис кожного завдання
        task_descriptions[index] = {'body': todo['body'], 'is_visible': False}

def toggle_description(index):
    """Перемикає видимість опису завдання без зміни позиції інших елементів."""
    if index in task_descriptions:
        task = task_descriptions[index]
        if task['is_visible']:
            # Видаляємо опис тільки якщо він був відкритий
            todos_list.delete(index + 1)
        else:
            # Вставляємо опис після завдання, якщо його ще немає
            todos_list.insert(index + 1, f"  Опис: {task['body']}")
        task['is_visible'] = not task['is_visible']

def add_todo():
    title = title_entry.get()
    body = body_entry.get()
    if title and body:
        create_todo(title, body)
        refresh_todos()
        title_entry.delete(0, tk.END)
        body_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Помилка", "Назва та опис не можуть бути порожніми")

def mark_complete():
    try:
        selected_index = todos_list.curselection()[0]
        complete_todo(selected_index + 1)
        refresh_todos()
    except IndexError:
        messagebox.showerror("Помилка", "Оберіть завдання для завершення")

def delete_selected():
    try:
        selected_index = todos_list.curselection()[0]
        delete_todo(selected_index + 1)
        refresh_todos()
    except IndexError:
        messagebox.showerror("Помилка", "Оберіть завдання для видалення")

def edit_selected():
    try:
        selected_index = todos_list.curselection()[0]
        new_title = title_entry.get()
        new_body = body_entry.get()
        if new_title and new_body:
            edit_todo(selected_index + 1, new_title, new_body)
            refresh_todos()
            title_entry.delete(0, tk.END)
            body_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Помилка", "Назва та опис не можуть бути порожніми")
    except IndexError:
        messagebox.showerror("Помилка", "Оберіть завдання для редагування")

def on_entry_click(event, entry, default_text):
    """Функція для зникнення тексту за замовчуванням при натисканні на поле."""
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg='white')  # Після натискання змінюємо колір тексту на білий

def on_focusout(event, entry, default_text):
    """Функція для повернення тексту за замовчуванням, якщо поле порожнє."""
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg='gray')  # Повертаємо колір тексту до сірого

def on_item_double_click(event):
    """Функція для обробки подвійного кліку на завданні та відображення опису."""
    try:
        selected_index = todos_list.curselection()[0]
        toggle_description(selected_index + 1)  # Відкриваємо/закриваємо опис для цього завдання
    except IndexError:
        messagebox.showerror("Помилка", "Оберіть завдання для перегляду")

# Головне вікно
root = tk.Tk()
root.title("To-Do Manager")
root.geometry("800x450")  # Збільшено розмір вікна для комфортного розташування елементів

# Стилізація темного фону та кольорів
root.configure(bg="#2C2C2C")

# Завантажуємо іконки для кнопок
icon_path_delete = "basket.png"  # Вказати шлях до вашої іконки для видалення
icon_delete = Image.open(icon_path_delete)
icon_delete = icon_delete.resize((20, 20))
icon_delete = ImageTk.PhotoImage(icon_delete)

icon_path_complete = "done.png"  # Вказати шлях до вашої іконки для завершення
icon_complete = Image.open(icon_path_complete)
icon_complete = icon_complete.resize((20, 20))
icon_complete = ImageTk.PhotoImage(icon_complete)

icon_path_add = "add.png"  # Вказати шлях до вашої іконки для додавання
icon_add = Image.open(icon_path_add)
icon_add = icon_add.resize((20, 20))
icon_add = ImageTk.PhotoImage(icon_add)

icon_path_edit = "redac.png"  # Вказати шлях до вашої іконки для редагування
icon_edit = Image.open(icon_path_edit)
icon_edit = icon_edit.resize((20, 20))
icon_edit = ImageTk.PhotoImage(icon_edit)

# Список завдань
todos_list = tk.Listbox(root, width=50, height=15, bg="#3A3A3A", font=("Arial", 12), selectbackground="#3A8DFF", selectmode=tk.SINGLE, bd=0, highlightthickness=0, fg="white")
todos_list.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
todos_list.bind("<Double-1>", on_item_double_click)  # Прив'язка подвійного кліку

# Поля для введення
title_default = "Введіть назву завдання"
title_entry = tk.Entry(root, width=30, font=("Arial", 12), bd=0, highlightthickness=0, bg="#444444", fg="gray")
title_entry.grid(row=0, column=1, padx=10, pady=5)
title_entry.insert(0, title_default)
title_entry.bind("<FocusIn>", lambda event: on_entry_click(event, title_entry, title_default))
title_entry.bind("<FocusOut>", lambda event: on_focusout(event, title_entry, title_default))

body_default = "Введіть опис завдання"
body_entry = tk.Entry(root, width=30, font=("Arial", 12), bd=0, highlightthickness=0, bg="#444444", fg="gray")
body_entry.grid(row=1, column=1, padx=10, pady=5)
body_entry.insert(0, body_default)
body_entry.bind("<FocusIn>", lambda event: on_entry_click(event, body_entry, body_default))
body_entry.bind("<FocusOut>", lambda event: on_focusout(event, body_entry, body_default))

# Кнопки в 2 стовпці
add_button = tk.Button(root, text="Додати", command=add_todo, font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", padx=20, pady=10, image=icon_add, compound="left")
add_button.grid(row=2, column=1, pady=10, sticky="w")

complete_button = tk.Button(root, text="Завершити", command=mark_complete, font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", padx=20, pady=10, image=icon_complete, compound="left")
complete_button.grid(row=3, column=1, pady=10, sticky="w")

delete_button = tk.Button(root, text="Видалити", command=delete_selected, font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", padx=20, pady=10, image=icon_delete, compound="left")
delete_button.grid(row=4, column=1, pady=10, sticky="w")

# Додаємо кнопку "Редагувати"
edit_button = tk.Button(root, text="Редагувати", command=edit_selected, font=("Arial", 12), bg="#FF9800", fg="white", relief="flat", padx=20, pady=10, image=icon_edit, compound="left")
edit_button.grid(row=5, column=1, pady=10, sticky="w")

# Оновлення списку
refresh_todos()

# Запуск програми
root.mainloop()
