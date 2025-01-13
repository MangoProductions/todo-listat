from remove import *
from viewtasks import *
from add_task import *

if __name__ == '__main__':

    tasks = []

    while True:
        print("\na  add_task\nb  view_tasks\nc  remove_task\nd  exit\n")    
        choice = input("choose:")

        if choice == "a":
            tasks = add_task(tasks)
        elif choice == "b":
            tasks = view_tasks(tasks)
        elif choice == "c":
            tasks = remove(tasks)
        elif choice == "d":
            break
        else:
            print("bad input, continuing.")



