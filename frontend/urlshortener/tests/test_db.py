import string

from django.test import TestCase

from urlshortener.db import generate_code, get_hash_by_url, get_url_by_hash
from urlshortener.models import Shortener


def validate_code(code, code_len):
    if len(code) != code_len:
        return False
    for c in code:
        if c not in string.ascii_lowercase + string.ascii_uppercase + string.digits:
            return False
    return True


class DBTestCase(TestCase):
    def test_generate_code(self):
        code_len = 8
        codes_number = 100
        codes_set = set()
        
        for i in range(codes_number):
            codes_set.add(generate_code(code_len))
        
        self.assertEqual(len(codes_set), codes_number)
        for code in codes_set:
            self.assertTrue(validate_code(code, code_len))

    def test_conversion(self):
        url = "https://www.google.ru/search?q=qwfeqwfqw&oq=qwfeqwfqw&sourceid=chrome&ie=UTF-8"

        self.assertTrue(get_url_by_hash(get_hash_by_url(url)), url)

    def test_get_url_by_random_hash(self):
        random_hash = "wWEFWFedw23"
        self.assertEqual(get_url_by_hash(random_hash), None)
