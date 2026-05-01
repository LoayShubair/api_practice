class User:
    def __init__(self, name):
        self.name = name


class Task:
    task_count = 0

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "open"
        self.onwer = None
        Task.task_count += 1

    def assign(self, user):
        self.onwer = user

    def complete(self):
        self.status = "done"

    def display(self):
        owner = self.onwer.name if self.onwer else "No owner"
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Owner: {owner}")
        print("-----")

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.title == other.title


User1 = User("Ali")
task1 = Task("Study Python", "Learn oop")
task2 = Task("Study python", "Practice more")

task1.assign(User1)
task1.complete()
task1.display
task2.display

print("are tasks equal?", task1 == task2)
print("total tasks:", Task.task_count)
