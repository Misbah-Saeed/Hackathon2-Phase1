class TaskManager:
    def __init__(self):
        self.tasks = []

    def update_task(self, index: int, new_description: str):
        """
        Update an existing task by index.
        """
        if not isinstance(index, int):
            raise ValueError("Task index must be an integer.")

        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")

        if not new_description.strip():
            raise ValueError("New task description cannot be empty.")

        self.tasks[index] = new_description
