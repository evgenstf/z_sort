import sqlite3

from file_article_storage import SQLArticleConnector
from sql_commands import SQLCommands

class SQLUserStorage:
    def __init__(self, sql_path):
        self.sql_path = sql_path
        self.sql_columns = ['owner', 'email', 'articles_id']

    def __get_articles_by_id_list(self, owner_articles_id_list):
        articles = []
        articles_connector = SQLArticleConnector(self.sql_path)
        for id in owner_articles_id_list:
            articles.append(articles_connector.get_article_by_id(id)[0])
        return articles

    def __delete_user(self, owner):
        connection = sqlite3.connect(self.sql_path)
        cursor = connection.cursor()
        sql_command = 'DELETE FROM users WHERE owner = "' + owner + '";'
        cursor.execute(sql_command)
        connection.commit()
        connection.close()
        return True

    def create_user(self, owner, email, articles_id = "[]"):
        connection = sqlite3.connect(self.sql_path)
        cursor = connection.cursor()
        sql_command = 'INSERT INTO users (owner, email, articles_id) VALUES ('
        sql_command += '"' + owner + '", '
        sql_command += '"' + email + '", '
        sql_command += '"' + articles_id + '");'
        cursor.execute(sql_command)
        connection.commit()
        connection.close()
        return True

    def get_articles_by_owner(self, owner):
        owner_data = SQLCommands.get_elements_from_sql_column_by_name(self.sql_path, 'users', 'owner', owner)[0]
        owner_articles_id_list = eval(owner_data['articles_id'])
        return self.__get_articles_by_id_list(owner_articles_id_list)

    def add_article_id_to_owner_articles_list(self, owner, article_id):
        owner_data = SQLCommands.get_elements_from_sql_column_by_name(self.sql_path, 'users', 'owner', owner)[0]
        if len(owner_data) == 0:
            self.create_user(owner, "")
            owner_data = SQLCommands.get_elements_from_sql_column_by_name(self.sql_path, 'users', 'owner', owner)[0]
        owner_articles_id_list = eval(owner_data['articles_id'])
        owner_articles_id_list.append(article_id)
        self.__delete_user(owner_data['owner'])
        self.create_user(owner_data['owner'], owner_data['email'], str(owner_articles_id_list))
        return True


