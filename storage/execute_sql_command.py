import sqlite3

def execute_sql_command(command):
    connection = sqlite3.connect(sql_path)
    cursor = connection.cursor()
    cursor.execute(command)
    results = cursor.fetchall()
    connection.close()
    output = []
    for result in results:
        output_dict = dict()
        for i in range(len(result)):
            output_dict[sql_columns[i]] = result[i]
        output.append(output_dict)
    return output
