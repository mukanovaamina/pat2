from decorator import Task, CompletedTaskDecorator

# Create list of task
task1 = Task("Do the assignment")
task2 = Task("Upload the assignment")

# Create decorators for task
completed_task1 = CompletedTaskDecorator(task1)
completed_task2 = CompletedTaskDecorator(task2)

# Complete task with using decorators
completed_task1.execute()
completed_task2.execute()
