class TaskManager:
    def __init__(self):
        self.tasks = []

    def view_task(self, index: int) -> str:
        """
        Return the task description at the given index.
        """
        if not isinstance(index, int):
            raise ValueError("Task index must be an integer.")

        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")

        return self.tasks[index]
