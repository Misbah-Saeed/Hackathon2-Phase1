class TaskManager:
    def __init__(self):
        self.tasks = []

    def delete_task(self, index: int):
        """
        Delete a task by its index.
        """
        if not isinstance(index, int):
            raise ValueError("Task index must be an integer.")

        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")

        del self.tasks[index]
