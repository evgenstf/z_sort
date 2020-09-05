from storage.file_article_storage import FileArticleStorage

class StorageTests:
    @staticmethod
    def file_article_storage_test():
        print('start file_article_storage_test')
        storage = FileArticleStorage('mock/file_article_storage_metafile.json')
        print('storage:', storage)
        print('articles:', storage.articles)
        for id, article in storage.articles.items():
            assert id == article.id
            print('id:', article.id)
            print('text:', article.text)
            print()

    @staticmethod
    def run_all():
        print('run storage tests')
        StorageTests.file_article_storage_test()
        print('finished\n')
