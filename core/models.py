from django.db import models


class Library(models.Model):
    """
        A code collection written for a specific language and purpose
        that makes implementing some goal easier. For example, Django is
        a library that eases creating Python web applications.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    homepage_url = models.URLField(max_length=1024)
    language = models.ForeignKey("ProgrammingLanguage")
    is_visible = models.BooleanField(default=False)


class ProgrammingLanguage(models.Model):
    """
        A programming language, such as Python or C, and related
        information on it.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    homepage_url = models.URLField(max_length=1024)
    is_visible = models.BooleanField(default=False)


class Paradigm(models.Model):
    """
        A programming paradigm, such as imperative or functional.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    is_visible = models.BooleanField(default=False)


class Tutorial(models.Model):
    """
        An article or blog post with a tutorial for a specific
        language or framework.
    """
    name = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=64, unique=True)
    homepage_url = models.URLField(max_length=2048)
    language = models.ForeignKey("ProgrammingLanguage")
    is_visible = models.BooleanField(default=False)

