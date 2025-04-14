# todo.py

FILENAME = "tasks.txt"

def show_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found. Starting fresh!")

def add_task(task):
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print(f"Added: {task}")

def delete_task(index):
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid task number!")
    except FileNotFoundError:
        print("No task file found.")

def main():
    while True:
        print("\n--- TO-DO APP ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
