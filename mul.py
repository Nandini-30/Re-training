def multiply(x,y):
    result=x*y
    return result

def getMul():
    x=int(input("enter the first number:"))
    y=int(input("enter the second number:"))
    z=multiply(x,y)
    print("Result is",z)

getMul();