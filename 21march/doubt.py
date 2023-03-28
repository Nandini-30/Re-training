import sqlite3
from emp import Employee

def getEmployeesByDeptId(id):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select name from employee where deptId = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)

        found=False
        l=[]
        for row in records:
            found=True
            e=row[0]
            l.append(e)
        print(l)

            
            
        if found==False:
            print("no empId found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        

getEmployeesByDeptId(2)