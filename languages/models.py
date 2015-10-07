from django.db import models

from taggit.managers import TaggableManager


class Library(models.Model):
    """
        A code library that implements some conceptual idea. For example,
        Django is an implementation of the web application framework
        concept.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    summary = models.TextField()
    homepage_url = models.URLField(max_length=1024)
    language = models.ForeignKey("ProgrammingLanguage")
    is_visible = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    """
        A programming language, such as Python or C, and related
        information on it.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    homepage_url = models.URLField(max_length=1024)
    summary = models.TextField()
    is_visible = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    """
        An article or blog post with a tutorial for a specific
        language or framework.
    """
    name = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=64, unique=True)
    summary = models.TextField()
    homepage_url = models.URLField(max_length=2048)
    language = models.ForeignKey("ProgrammingLanguage")
    is_visible = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.name

