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
    homepage_url = models.URLField(max_length=1024, blank=True, default="")
    package_url = models.URLField(max_length=2048, blank=True, default="")
    source_code_url = models.URLField(max_length=2048, blank=True,
                                      default="")
    summary = models.TextField()
    language = models.ForeignKey("Language")
    is_visible = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "libraries"


class Language(models.Model):
    """
        A programming language, such as Python or C, and related
        information on it.
    """
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=64, unique=True)
    homepage_url = models.URLField(max_length=1024, blank=True)
    summary = models.TextField()
    year_appeared = models.IntegerField(null=True, blank=True)
    source_code_url = models.URLField(max_length=2048, blank=True,
                                      default="")
    logo_url = models.URLField(max_length=2048, blank=True)
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
    tutorial_url = models.URLField(max_length=2048)
    language = models.ForeignKey("Language", related_name="tutorials",
                                 blank=True, null=True)
    libraries = models.ManyToManyField("Library", related_name="tutorials",
                                       blank=True)
    summary = models.TextField()
    is_visible = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):
        return self.name

