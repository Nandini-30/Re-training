class employee:
    def __init__(self,name,deptid,address):
        self.name = name
        self.deptid = deptid
        self.address = address
    
    def __repr__(self):
        return f"name:{self.name},dept_id:{self.deptid},address:{self.address}"

class employeeStatus():
    
    def __init__(self,statuscode,message,empobj):
        self.statuscode = statuscode
        self.message = message
        self.empobj = empobj
    
    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.empobj}"