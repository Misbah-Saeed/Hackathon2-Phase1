class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str):
        if not description.strip():
            raise ValueError("Task description cannot be empty.")
        self.tasks.append(description)

    def delete_task(self, index: int):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        self.tasks.pop(index)

    def update_task(self, index: int, new_description: str):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        if not new_description.strip():
            raise ValueError("Task description cannot be empty.")
        self.tasks[index] = new_description

    def view_task(self, index: int) -> str:
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        return self.tasks[index]

    def mark_complete(self, index: int):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        if "[Completed]" not in self.tasks[index]:
            self.tasks[index] += " [Completed]"

    def list_tasks(self):
        return self.tasks
