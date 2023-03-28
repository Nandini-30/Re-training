import sqlite3
from emp_model import employee,employeeStatus

def insertemployee(t):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        
        sqlite_insert_query = """INSERT INTO employee
                     (empno,empname,deptid,address)
                     VALUES
                     (?,?,?,?)"""
        
        data_tuple = (t.num,t.name,t.deptid,t.address)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()
        
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            
def getEmployeeInfo(num):
    es = employeeStatus(0,"Not found",None)
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        
        sql_select_query = """select * from employee where empno = ?"""
        cursor.execute(sql_select_query, (num,))
        records = cursor.fetchall()
        
        found = False
        for row in records:
            t = employee(row[0],row[1],row[2],row[3])
            es.statuscode = 1
            es.message = "Employee Found"
            es.empobj = t
            
        cursor.close()
            
    except sqlite3.Error as error:
        es.message = f"{error}"
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
        return es
    
def getDeptInfo(id):
    el = []
        
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        
        sql_select_query = """select * from employee where deptid = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        
        for row in records:
            t = employee(row[0],row[1],row[2],row[3])
            el.append(t)
            
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return el