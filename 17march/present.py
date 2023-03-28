from logic import addTask, viewTask, present ,updateTask

def start():
    exit = False
    while(exit == False):
        print("\n1.Task operation:, \n2.0.Exit")
        ch = int (input("Enter choice: "))

        if ch == 1:
            c = int(input("Enter task id: "))
            task()

        elif ch == 0:
            exit = True


def task(c):
    exit = False
    while(exit == False):
        id = int(input("Enter id: "))
        p = present(id)
        if p == 1:
            print("\n1.Update task info \n2.View task info \n3.Remove task info n4.exit")
            ch = int(input("Enter Your choice: "))

            if ch == 1:
                a = input("Enter new task name: ")
                b = input("Enter new task desc: ")
                c = input("Enter new task priority: ")
                task = task(b,c,d)
                message = updateTask(id,task)
                print(message)
            
            elif ch == 2:
                a = input ("Enter task id: ")
                message = viewTask(a)
                print(message)

            if ch == 0:
                exit = True

        else:
            print("No such task...create one")
            b = input("Enter task name: ")
            c = input("Enter task desc: ")
            d = input ("Enter task priority: ")
            t1 = task(b,c,d)
            message = addTask(id,t1)
            print(message)
                    

        