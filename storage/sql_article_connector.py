import sqlite3

from storage.execute_sql_command import execute_sql_command

SELECT_TOP10_ARTICLES = 'SELECT * FROM articles LIMIT 10;'
SELECT_ARTICLE_BY_AUTHOR = 'SELECT * FROM articles WHERE authors like \'%"{author}"%\';'
SELECT_ARTICLE_BY_ID = 'SELECT * FROM articles WHERE id = "{id}";'
SELECT_ARTICLE_BY_TAG = 'SELECT * FROM articles WHERE tag = "{tag}";'
SELECT_ARTICLE_BY_CATEGORY = 'SELECT * FROM articles WHERE category = "{category}";'

ADD_NEW_ARTICLE = """
    INSERT INTO articles (id, header, date, authors, tags, category, sections, html, preview_html)
    VALUES ({id}, '{header}', '{date}', '{authors}', '{tags}', '{category}', '{sections}', '{html}', '{preview_html}');
"""

SELECT_NEXT_ID = 'SELECT ifnull(max(id) + 1, 0) FROM articles;'

def esq(string):
    return string.replace("'", '<single-quote>')

def desq(string):
    return string.replace('<single-quote>', "'")

def convert_article_row_to_dict(row):
    columns = ['id', 'header', 'date', 'authors', 'tags', 'category', 'sections', 'html', 'preview_html']
    article = {}
    for index, data in enumerate(row):
        if type(data) == str:
            data = desq(data)
        article[columns[index]] = data

    return article

def convert_article_rows_to_dicts(rows):
    articles = []
    for row in rows:
        articles.append(convert_article_row_to_dict(row))

    return articles



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
            category=esq(article['category']),
            html=esq(article['html']),
            preview_html=esq(article['preview_html'])
        )
        return execute_sql_command(command)

    @staticmethod
    def get_top10_articles():
        output_rows = execute_sql_command(SELECT_TOP10_ARTICLES)
        return convert_article_rows_to_dicts(output_rows)


    @staticmethod
    def get_articles_by_author(owner):
        return execute_sql_command(SELECT_ARTICLE_BY_AUTHOR.format(author=esq(author)))

    @staticmethod
    def get_article_by_id(id):
        return execute_sql_command(SELECT_ARTICLE_BY_ID.format(id=esq(id)))

    @staticmethod
    def get_articles_by_tag(tag):
        output_rows = execute_sql_command(SELECT_ARTICLE_BY_TAG.format(tag=esq(tag)))
        return convert_article_rows_to_dicts(output_rows)

    @staticmethod
    def get_articles_by_category(category):
        print("category:", category)
        output_rows = execute_sql_command(SELECT_ARTICLE_BY_CATEGORY.format(category=esq(category)))
        return convert_article_rows_to_dicts(output_rows)

    @staticmethod
    def get_next_article_id():
        raw_output = execute_sql_command(SELECT_NEXT_ID)
        return raw_output[0][0]
