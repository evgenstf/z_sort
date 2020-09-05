from article_manager.article_manager import *

class ArticleManagerTests:
    @staticmethod
    def simple_test():
        print('start simple test')
        manager = ArticleManager()
        print('manager:', manager)

    @staticmethod
    def run_all():
        print('run article_manager tests')
        ArticleManagerTests.simple_test()
        print('finished\n')
