d = {}

def present(id):
    if d.get(id) is not None:
        return 1
    else:
        return 0
    
def addTask(id,t1):
    d[id] = t1
    return d

def viewTask(a):
    return a

def updateTask(id,b):
    d[id] = b
    return "Task Updated"