# Base class Task
class Task:
    def __init__(self, description):
        self.description = description

    # Меthod execute displays a message
    def execute(self):
        print(f"The task is completing: {self.description}")

#create class CompletedTaskDecorator
class CompletedTaskDecorator:
    def __init__(self, task):
        self.task = task

    # Мethod execute call a base task and adds additional functionality
    def execute(self):
        self.task.execute()
        self.mark_completed()

    def mark_completed(self):
        # Мethod mark_completed() add mark
        print(f"Task is completed: {self.task.description}")
