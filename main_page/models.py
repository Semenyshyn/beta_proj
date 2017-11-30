from django.db import models


class Messages(models.Model):
    method = models.CharField(max_length=1000, default=None)
    body = models.CharField(max_length=1000, default=None)
    encoding = models.CharField(max_length=1000, default=None)
    content_type = models.CharField(max_length=1000, default=None)


