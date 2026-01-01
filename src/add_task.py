# src/add_task.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        """
        Adds a new task to the list.

        Args:
            task_description (str): The description of the task.

        Raises:
            ValueError: If the task description is empty.
        """
        if not task_description.strip():
            raise ValueError("Task description cannot be empty.")

        self.tasks.append(task_description)

    def get_tasks(self):
        """
        Returns the list of tasks.

        Returns:
            list: The current list of tasks.
        """
        return self.tasks


# Standalone function to integrate with app.py
def add_task(tasks):
    task_description = input("Enter task description: ")
    if not task_description.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks.append(task_description)
    print(f"Task added: {task_description}")
