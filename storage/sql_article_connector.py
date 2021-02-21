import sqlite3

from storage.execute_sql_command import execute_sql_command

SELECT_TOP10_ARTICLES = 'SELECT * FROM articles LIMIT 10;'
SELECT_ARTICLE_BY_AUTHOR = 'SELECT * FROM articles WHERE authors like \'%"{author}"%\';'
SELECT_ARTICLE_BY_ID = 'SELECT * FROM articles WHERE id = "{id}";'
SELECT_ARTICLE_BY_TAG = 'SELECT * FROM articles WHERE tag = "{tag}";'

ADD_NEW_ARTICLE = """
    INSERT INTO articles (id, header, date, authors, tags, sections, html)
    VALUES ({id}, '{header}', '{date}', '{authors}', '{tags}', '{sections}', '{html}');
"""

SELECT_NEXT_ID = 'SELECT ifnull(max(id) + 1, 0) FROM articles;'

def esq(string):
    return string.replace("'", '<single-quote>')

def desq(string):
    return string.replace('<single-quote>', "'")

class SQLArticleConnector:
    @staticmethod
    def add_new_article(article):
        command = ADD_NEW_ARTICLE.format(
            id=article['id'],
            header=esq(article['header']),
            date=esq(article['date']),
            authors=esq(article['authors']),
            sections=esq(article['sections']),
            tags=esq(article['tags']),
            html=None
        )
        return execute_sql_command(command)

    @staticmethod
    def get_top10_articles():
        raw_output = execute_sql_command(SELECT_TOP10_ARTICLES)
        print('raw_output:', raw_output)
        return []


    @staticmethod
    def get_articles_by_author(owner):
        return execute_sql_command(SELECT_ARTICLE_BY_AUTHOR.format(author=esq(author)))

    @staticmethod
    def get_article_by_id(id):
        return execute_sql_command(SELECT_ARTICLE_BY_ID.format(id=esq(id)))

    @staticmethod
    def get_articles_by_tag(tag):
        raw_output = execute_sql_command(SELECT_ARTICLE_BY_TAG.format(tag=esq(tag)))
        articles = []

        return articles

    @staticmethod
    def get_next_article_id():
        raw_output = execute_sql_command(SELECT_NEXT_ID)
        return raw_output[0][0]
