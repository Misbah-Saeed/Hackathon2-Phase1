class TaskManager:
    def __init__(self):
        self.tasks = []

    def mark_complete(self, index: int):
        """
        Mark a task as complete by appending '[Completed]' to it.
        """
        if not isinstance(index, int):
            raise ValueError("Task index must be an integer.")

        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")

        if "[Completed]" not in self.tasks[index]:
            self.tasks[index] += " [Completed]"
