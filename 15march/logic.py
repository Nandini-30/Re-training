import random

randomlist = []

def randomList():
    for i in range(0,10):
        n= random.randint(0,50)
        randomlist.append(n)

def view():
    return randomlist

def change(a,b):
    if a not in randomlist:
        return "Number not in list"
    elif b in randomlist:
        return "Number already in list"

    else:
        i = randomlist.index(a)
        randomlist[i] = b
        return "Number Changed"
    
def removeelem(ele):
    if ele in randomlist:
        randomlist.remove(ele)
        return "Number Removed"
    else:
        return"No such Number"
    
def acs():
    acs = randomlist.copy()
    acs.sort()
    return acs
    
def des():
    des= randomlist.copy()
    des.sort(reverse=True)
    return des
            