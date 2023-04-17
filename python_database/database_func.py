import sqlite3

#Function to quickly print Queries from DB
def printQuery(query):
    data_conn = sqlite3.connect('./python_database/Diseases.db')
    c = data_conn.cursor()
    c.execute(query)
    print("\nQuery:")
    for item in c.fetchall():
        print(str(item))
    data_conn.close()

#Functino to add column to a table (You guys probably wont need this)
def addColumn(table_name, column_name, column_def):
    cars_conn = sqlite3.connect('./python_database/Diseases.db')
    c = cars_conn.cursor()
    c.execute(" ALTER TABLE " + table_name + " ADD " + column_name + " " + column_def )
    cars_conn.commit()
    cars_conn.close()

#Function to make query to DB and store it into a Python variable
def storeQueryToVar(query):
    data_conn = sqlite3.connect('./python_database/Diseases.db')
    value = []
    c = data_conn.cursor()
    c.execute(query)
    for item in c.fetchall():
        value.append(item)
    data_conn.close()
    return value