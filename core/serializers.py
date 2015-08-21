from rest_framework import serializers

from core.models import ProgrammingLanguage, Paradigm


class ProgrammingLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ('name', 'slug', 'homepage_url',)


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('name', 'slug')

