import sqlite3

def execute_sql_command(command):
    connection = sqlite3.connect('../db.sqlite3')
    cursor = connection.cursor()
    cursor.execute(command)
    output = cursor.fetchall()
    connection.commit()
    connection.close()
    return output
