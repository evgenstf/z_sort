import sqlite3

from storage.execute_sql_command import execute_sql_command

SELECT_ALL_ARTICLE = 'SELECT * FROM articles;'
SELECT_ARTICLE_BY_OWNER = 'SELECT * FROM articles WHERE owner = "{owner}";'
SELECT_ARTICLE_BY_ID = 'SELECT * FROM articles WHERE id = "{id}";'

ADD_NEW_ARTICLE = """
    INSERT INTO articles (id, header, date, owner, sections, html)
    VALUES ({id}, {header}, {date}, {owner}, {sections}, {html});
"""

class SQLArticleConnector:
    def __init__(self, sql_path):
        self.sql_path = sql_path
        self.sql_columns = ['id', 'header', 'date', 'owner', 'article', 'html']

    def add_new_article(self, article):
        command = ADD_NEW_ARTICLE.format(
            id=article['id'],
            header=article['header'],
            date=article['date'],
            owner=article['owner'],
            sections=article['sections'],
            html=article['html']
        )
        return execute_sql_command(command)

    def get_articles_by_owner(self, owner):
        return execute_sql_command(SELECT_ARTICLE_BY_OWNER.format(owner=owner))

    def get_article_by_id(self, id):
        return execute_sql_command(SELECT_ARTICLE_BY_ID.format(id=id))
