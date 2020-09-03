import random
import string

from urlshortener.models import Shortener, SHORTENED_CODE_LENGTH, URL_MAX_LENGTH


def generate_code(code_len):
    allowed_symbols = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    result = []
    for i in range(code_len):
        index = random.randint(0, len(allowed_symbols) - 1)
        result.append(allowed_symbols[index])
    return "".join(result)
    
def get_hash_by_url(url):
    assert(len(url) <= URL_MAX_LENGTH)

    unique_code = generate_code(SHORTENED_CODE_LENGTH)
    
    Shortener.objects.create(url=url, shortened_code=unique_code)

    return unique_code

def get_url_by_hash(shortened_code):
    url_object = None
    try:
        url_object = Shortener.objects.get(shortened_code=shortened_code)
    except Shortener.DoesNotExist:
        return None

    return url_object.url
