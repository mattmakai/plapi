from django.db import models


class Concept(models.Model):
    """
        A conceptual idea related to programming, such as web application
        framework, task queue, file system or concurrency model.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    summary = models.TextField()
    language = models.ManyToManyField("ProgrammingLanguage")
    is_visible = models.BooleanField(default=False)

    def __str(self):
        return self.name


class Implementation(models.Model):
    """
        An implementation of a conceptual idea in a particular programming
        language represented as a code collection. For example, Django is
        an implementation of the web application framework concept.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    summary = models.TextField()
    homepage_url = models.URLField(max_length=1024)
    language = models.ForeignKey("ProgrammingLanguage")
    is_visible = models.BooleanField(default=False)

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

    def __str__(self):
        return self.name


class Paradigm(models.Model):
    """
        A programming paradigm, such as imperative or functional.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    summary = models.TextField()
    is_visible = models.BooleanField(default=False)

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

    def __str__(self):
        return self.name

