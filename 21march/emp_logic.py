from emp import Employee,EmployeeStatus
from emp_db import getDeveloperInfo,getEmployeesByDeptId

def viewDetails(n):
    e=getDeveloperInfo(n)
    if e is not None:
        return EmployeeStatus(1,"Found",e)
    else:
        return EmployeeStatus(0,"Not Found",None)

def viewEmployees(n):
    e=getEmployeesByDeptId(n)
    return(e)
    
