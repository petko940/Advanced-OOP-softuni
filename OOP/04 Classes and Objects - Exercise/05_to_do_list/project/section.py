from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for x in self.tasks:
            if x.name == task_name:
                x.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for x in self.tasks:
            if x.completed:
                self.tasks.remove(x)
                count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]
        for x in self.tasks:
            output.append(x.details())
        return '\n'.join(output)
