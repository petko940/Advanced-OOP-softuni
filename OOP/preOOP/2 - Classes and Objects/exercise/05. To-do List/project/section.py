from project.task import Task


class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for x in self.tasks:
            if x.name == task_name:
                x.completed = True
                return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount = 0
        for x in range(len(self.tasks) - 1, -1 , -1):
            if self.tasks[x].completed:
                amount += 1
                self.tasks.pop(x)
        return f"Cleared {amount} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]
        for x in self.tasks:
            output.append(x.details())
        return "\n".join(output)


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
