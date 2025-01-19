import json
import os

def load_tasks():
    """Загружает задачи из файла tasks.json, если он существует."""
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []


def save_tasks(tasks):
    """Сохраняет задачи в файл tasks.json."""
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    """Добавляет новую задачу в список."""
    task_name = input("Введите название задачи: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Задача '{task_name}' добавлена.")


def list_tasks(tasks):
    """Выводит список задач с их статусом."""
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for i, task in enumerate(tasks):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task['name']}")

def mark_task_completed(tasks):
    """Помечает задачу как выполненную."""
    list_tasks(tasks)
    try:
        task_index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Задача отмечена как выполненная.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите номер задачи.")

def delete_task(tasks):
     """Удаляет задачу из списка."""
     list_tasks(tasks)
     try:
         task_index = int(input("Введите номер задачи для удаления: ")) - 1
         if 0 <= task_index < len(tasks):
            task_name = tasks[task_index]["name"]
            del tasks[task_index]
            print(f"Задача '{task_name}' удалена.")
         else:
             print("Неверный номер задачи.")
     except ValueError:
          print("Пожалуйста, введите номер задачи.")


def main():
    tasks = load_tasks()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Список задач")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

        save_tasks(tasks)

if __name__ == "__main__":
    main()
