import json
import os

TODO_FILE = 'todo_list.json'

# Load tasks from file if exists
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("✅ Your to-do list is empty!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task['done'] else "❌"
            print(f"{i}. {task['task']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    task_desc = input("Enter the task: ").strip()
    if task_desc:
        tasks.append({'task': task_desc, 'done': False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            print("Marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
