from django.db import models


URL_MAX_LENGTH = 4096
SHORTENED_CODE_LENGTH = 8

class Shortener(models.Model):
    url = models.CharField(max_length=URL_MAX_LENGTH)
    shortened_code = models.CharField(max_length=SHORTENED_CODE_LENGTH)
