import sqlite3

class SQLCommands:
    @staticmethod
    def get_elements_from_sql_column_by_name(sql_path, table_name, column, name):
        sql_columns = ['owner', 'email', 'articles_id']
        connection = sqlite3.connect(sql_path)
        cursor = connection.cursor()
        sql_command = 'SELECT * FROM ' + table_name + ' WHERE ' + column + ' = "'  + name + '";'
        cursor.execute(sql_command)
        results = cursor.fetchall()
        connection.close()
        output = []
        for result in results:
            output_dict = dict()
            for i in range(len(result)):
                output_dict[sql_columns[i]] = result[i]
            output.append(output_dict)
        return output
