from logic2 import randomList, view, change, removeelem, acs ,des

def fillList():
    randomList()
    print("filled 10 random nos::")
    print()

def viewList():
    message = view()
    print(message)
    print()

def changeNum():

    a =int(input("enter the number::"))
    b =int(input("enter tne new number::"))

    message = change(a,b)
    print(message)
    print()

def remove():
    ele = int(input("enter the number to remove::"))
    message = removeelem(ele)
    print(message)
    print()

def sortacs():
    message =acs()
    print(message)

def sortdes():
    message = des()
    print(message)

def init():

    exit = False

    while exit == False:
        print("1. fill up list with 10 random number")
        print("2.View all the list")
        print("3.Change the no")
        print("4.Remove element")
        print("5.Sort in ascending")
        print("6.Sort in descending")
        print("0.exit")

        ch = int(input("enter choice::"))
        if ch == 1:
            fillList()

        elif ch == 2:
            viewList()

        elif ch == 3:
            changeNum()

        elif ch == 4:
            remove()  

        elif ch == 5:
            sortacs()

        elif ch == 6:
            sortdes()

        elif ch == 0:
            break

            


