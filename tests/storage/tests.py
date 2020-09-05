from storage.storage import *

class StorageTests:
    @staticmethod
    def simple_test():
        print('start simple test')
        storage = Storage()
        print('storage:', storage)

    @staticmethod
    def run_all():
        print('run storage tests')
        StorageTests.simple_test()
        print('finished\n')
