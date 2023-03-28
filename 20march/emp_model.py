class Employee():
    def __init__(self,empno,name,age,deptId):
        self.empno=empno
        self.name=name
        self.age=age
        self.deptId=deptId

    def __str__(self):
        return f"EmpID: {self.empno}\nName: {self.name}\nAge: {self.age}\nDepartment ID: {self.deptId}"
class EmployeeStatus():
    def __init__(self,statusCode,message,empObj):
        self.statusCode=statusCode
        self.message=message
        self.empObj=empObj

    # def __str__(self):
    #     return f"Status Code: {self.statusCode}\nMessage: {self.message}\nEmployee Details: {self.empObj}"