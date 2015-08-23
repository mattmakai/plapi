from rest_framework import serializers

from .models import (Concept, Implementation, ProgrammingLanguage,
                     Paradigm, Tutorial,)


class ConceptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concept
        fields = ('name', 'slug', 'language', 'summary',)


class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implementation
        fields = ('name', 'slug', 'language', 'summary',)


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

