import argparse
from todoman import show_all_todos, show_todo, create_todo, complete_todo, delete_todo, edit_todo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To Do Application")
    subparsers = parser.add_subparsers(dest="command")

    # Підкоманда для перегляду всіх завдань
    subparsers.add_parser("show-all", help="Показати всі завдання")

    # Підкоманда для перегляду конкретного завдання
    show_parser = subparsers.add_parser("show", help="Показати конкретне завдання")
    show_parser.add_argument("--index", type=int, required=True, help="Індекс завдання")

    # Підкоманда для створення нового завдання
    create_parser = subparsers.add_parser("create", help="Створити нове завдання")
    create_parser.add_argument("--title", type=str, required=True, help="Назва завдання")
    create_parser.add_argument("--body", type=str, required=True, help="Опис завдання")

    # Підкоманда для завершення завдання
    complete_parser = subparsers.add_parser("complete", help="Завершити завдання")
    complete_parser.add_argument("--index", type=int, required=True, help="Індекс завдання")

    # Підкоманда для видалення завдання
    delete_parser = subparsers.add_parser("delete", help="Видалити завдання")
    delete_parser.add_argument("--index", type=int, required=True, help="Індекс завдання")

    # Підкоманда для редагування завдання
    edit_parser = subparsers.add_parser("edit", help="Редагувати завдання")
    edit_parser.add_argument("--index", type=int, required=True, help="Індекс завдання")
    edit_parser.add_argument("--title", type=str, required=True, help="Нова назва завдання")
    edit_parser.add_argument("--body", type=str, required=True, help="Новий опис завдання")

    args = parser.parse_args()

    if args.command == "show-all":
        show_all_todos()
    elif args.command == "show":
        show_todo(args.index)
    elif args.command == "create":
        create_todo(args.title, args.body)
    elif args.command == "complete":
        complete_todo(args.index)
    elif args.command == "delete":
        delete_todo(args.index)
    elif args.command == "edit":
        edit_todo(args.index, args.title, args.body)
    else:
        parser.print_help()