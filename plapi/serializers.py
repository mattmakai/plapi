from rest_framework import serializers

from core.models import ProgrammingLanguage


class ProgrammingLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ('name', 'slug', 'homepage_url',)

