def getSum(num1,num2):
    result = num1+num2
    return result

def sum():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    i = getSum(num1,num2)
    print('addition is', i)

sum();