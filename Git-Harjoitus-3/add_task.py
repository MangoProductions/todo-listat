#Add Task
lista = []
def add_task(lista):
    while True:
        task_x = input("Anna tehtävän nimike: ")
        print("Kiitos tehtävästä")
        break
    lista.append(task_x)
    return lista
