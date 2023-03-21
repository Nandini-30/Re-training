def count(x,y):
    result = x.count(y)
    return result
def start():
    X = input("Enter the first string: ")
    Y = input("Enter the second string: ")
    count = X.count(Y)
    if count == 0:
        print("-1")
    else:
        print("The number of times '{}' appears in '{}' is: {}".format(Y, X, count))
        
start();