#the code for view tasks 

def view_tasks(list):
        """Display all tasks with their indices"""
        for index, task in enumerate(list):
            print(f"{index + 1}. {task}")