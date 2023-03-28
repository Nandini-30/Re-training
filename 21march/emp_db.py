import sqlite3
from emp import Employee

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from employee where empId = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()

        for row in records:
            e=Employee(row[0],row[1],row[2],row[3])
            return (e)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def getEmployeesByDeptId(id):
    employeelist=[]
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select name from employee where deptId = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()


        for row in records:
            e=row[0]
            employeelist.append(e)
        
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return employeelist