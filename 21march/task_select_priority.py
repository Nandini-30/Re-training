import sqlite3
from task import Task

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from task where priority = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)

        found=False
        l=[]
        for row in records:
            found=True
            t=Task(row[0],row[1],row[2])
            l.append(t)
            # print("taskid  = ", row[0])
            # print("taskname  = ", row[1])
            # print("priority  = ", row[2])
        print(l)
            # print("***")
            
            
            
        if found==False:
            print("no itemno found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(5)