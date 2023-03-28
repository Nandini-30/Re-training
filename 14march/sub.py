def subtract(x,y):
    result=x-y
    return result


def getSub():
    x= int(input("Enter the first number:"))
    y= int(input("Enter the second number:"))
    z=subtract(x,y)
    print("result is",z)

getSub();