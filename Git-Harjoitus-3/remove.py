
def remove(arr):
    index = input("task to be removed: ")
    try:
        index = int(index)
    except ValueError:
        print("bad value, nothing was removed")
        index = -1

    return [elem for i, elem in enumerate(arr) if i!=index-1]


