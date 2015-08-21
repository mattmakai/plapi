from django.db import models


class ProgrammingLanguage(models.Model):
    """
        A programming language, such as Python or C, and related
        information on it.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64)
    homepage_url = models.URLField(max_length=1024)
    is_visible = models.BooleanField(default=False)


class Paradigm(models.Model):
    """
        A programming paradigm, such as imperative or functional.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64)
    is_visible = models.BooleanField(default=False)
