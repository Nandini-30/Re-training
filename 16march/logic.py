d={}
def add(w):
    if d.get(w)==None:
        d[w]=1
    else:
        d[w]+=1
    return "---Word added---"

def view():
    v=list(d.keys())
    return v

def viewAll():
    return d

def viewDesired(n):
    list=[]
    for i in d:
        if d[i]==n:
            list.append(i)
    return list