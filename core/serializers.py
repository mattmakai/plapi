from rest_framework import serializers

from core.models import Library, ProgrammingLanguage, Paradigm, Tutorial


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('name', 'slug', 'homepage_url', 'language', 'summary',)

class ProgrammingLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ('name', 'slug', 'homepage_url', 'summary',)


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('name', 'slug', 'language', 'summary',)


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('name', 'slug', 'homepage_url', 'language', 'summary',)

