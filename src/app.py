from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- TODO APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                task = input("Enter task: ")
                manager.add_task(task)

            elif choice == "2":
                for i, task in enumerate(manager.list_tasks()):
                    print(f"{i}. {task}")

            elif choice == "3":
                i = int(input("Task index: "))
                new = input("New description: ")
                manager.update_task(i, new)

            elif choice == "4":
                i = int(input("Task index: "))
                manager.delete_task(i)

            elif choice == "5":
                i = int(input("Task index: "))
                manager.mark_complete(i)

            elif choice == "6":
                print("Goodbye 👋")
                break

            else:
                print("Invalid choice!")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
