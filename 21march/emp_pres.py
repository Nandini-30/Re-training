from emp_logic import viewDetails,viewEmployees

exit=False
def run():
    while exit==False:
        print("-------------------------------")
        print("****Main Menu****")
        print("1.View Employee Details")
        print("2.View employees based on deptId")
        print("0.Exit")
        print("-------------------------------")
        c=int(input("Enter your choice: "))
        print("-------------------------------")
        choice(c)

def choice(c):
    if c==1:
        n=int(input("Enter employee ID:"))
        res=viewDetails(n)
        if res.statusCode==1:
            print(f"Status Code: {res.statusCode}\nMessage: {res.message}\nEmployee Details: {res.empObj}")
        else:
            print(f"Status Code: {res.statusCode}\nMessage: {res.message}\nEmployee Details: {res.empObj}")
    elif c==2:
        n=int(input("Enter Department ID:"))
        res=viewEmployees(n)
        if len(res) is not 0:
            for i in res:
                print(i)
        else:
            print("No employees found")
    elif c==0:
        global exit
        exit=True