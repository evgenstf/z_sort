from storage.file_article_storage import FileArticleStorage

class StorageTests:
    @staticmethod
    def file_article_storage_test():
        print('start file_article_storage_test')
        storage = FileArticleStorage('mock/articles.meta')
        assert storage.metapath == 'mock/articles.meta'
        print('storage.article_paths', storage.article_paths)
        assert storage.article_paths == {'mock/articles/sample_1/article.md', 'mock/articles/sample_2/article.md'}

    @staticmethod
    def run_all():
        print('run storage tests')
        StorageTests.file_article_storage_test()
        print('finished\n')
