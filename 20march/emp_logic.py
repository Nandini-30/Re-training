from emp_model import Employee,EmployeeStatus
emp1=Employee(1,"ram",23,1)
emp2=Employee(2,"neha",25,1)
emp3=Employee(3,"rishi",22,2)
emp4=Employee(4,"kiran",21,2)
emp5=Employee(5,"kabir",22,3)

d={emp1.empno:emp1,emp2.empno:emp2,emp3.empno:emp3,emp4.empno:emp4,emp5.empno:emp5}

def viewDetails(n):
    if d.get(n) is not None:
        return EmployeeStatus(1,"Found",d[n])
    else:
        return EmployeeStatus(0,"Not Found",None)

def viewEmployees(n):
    l=[]
    for i in d.values():
        if i.deptId==n:
            l.append(i.name)
    return l
