import sqlite3

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from item where itemno = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)

        found=False
        # l=[]
        for row in records:
            found=True
            # t=Task()
            # l.append(t) 
            print("itemno  = ", row[0])
            print("itemname  = ", row[1])
            print("price  = ", row[2])
            print("category  = ", row[3])
            
        if found==False:
            print("no itemno found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(1)