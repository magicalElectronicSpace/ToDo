import json
from pathlib import Path

class ToDoApp:
    def __init__(self):
        self.data_path = Path(__file__).parent / 'data.json'
        self.data = {}
        self.file = "N/A"
        self.todoList = []
        if self.data_path.exists():
            with open(self.data_path, "r") as f:
                self.data = json.loads(f.read())
        if self.data["lastUsedFile"] == "N/A":
            self.file = input("Enter the name of the file you want to use: ")
        else:
            self.file = self.data["lastUsedFile"]
        self.load()
    def load(self):
        if not Path(self.file).exists():
            with open(self.file, "w") as f:
                f.write(json.dumps([]))
        with open(self.file, "r") as f:
            self.todoList = json.loads(f.read())

    
    def write(self):
        with open(self.file, "w") as f:
            f.write(json.dumps(self.todoList))
        self.data["lastUsedFile"] = self.file
        self.data_path.write_text(json.dumps(self.data))

    def list(self):
        print("To-Do List:")
        for i, task in enumerate(self.todoList):
            print(f"{i + 1}. {task['name']} - {'✅' if task['done'] else '❌'}")
    
    def add(self):
        task = {"name": input("Enter the task: "), "done": False}
        self.todoList.append(task)
        self.write()
    
    def complete(self, task):
        for task in self.todoList:
            if task["name"] == task:
                task = task
        task["done"] = True
        self.write()

    def uncomplete(self, task):
        for task in self.todoList:
            if task["name"] == task:
                task = task
        task["done"] = False
        self.write()
    
    def remove(self, task):
        for task in self.todoList:
            if task["name"] == task:
                task = task
        self.todoList.remove(task)
        self.write()
    
    def delete_file(self):
        if Path(self.file).exists():
            Path(self.file).unlink()
            print(f"File '{self.file}' deleted.")
            self.data["lastUsedFile"] = "N/A"
            self.data_path.write_text(json.dumps(self.data))
            self.file = input("Enter the name of the new file you want to use: ")
            self.load()
        else:
            print(f"File '{self.file}' does not exist.")
    
    def run(self):
        print("Welcome to the To-Do App!")
        print("Please select an option:")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Change file")
        print("4. Complete task")
        print("5. Remove Task")
        print("6. Uncomplete Task")
        print("7. Delete current file")
        print("8. Exit")
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add()
            elif choice == "2":
                self.list()
            elif choice == "3":
                self.file = input("Enter the name of the file you want to use: ")
                self.load()
            elif choice == "4":
                self.complete(input("Enter the task name: "))
            elif choice == "5":
                self.remove(input("Enter the task name: "))
            elif choice == "6":
                self.uncomplete(input("Enter the task name: "))
            elif choice == "7":
                self.delete_file()
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")
        self.write()
        print("Thank you for using the To-Do App!")
