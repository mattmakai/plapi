from rest_framework import reverse, serializers
from rest_framework.serializers import HyperlinkedRelatedField

from .models import Library, Language, Tutorial


"""
class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('name', 'slug', 'language', 'summary', 'url',)
        lookup_field = 'slug'
"""

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='language-detail', lookup_field='slug'
    )
    tutorials = HyperlinkedRelatedField(many=True, read_only=True,
                                        view_name='tutorial-detail',
                                        lookup_field='slug')

    class Meta:
        model = Language
        fields = ('name', 'url', 'homepage_url', 'summary', 'tutorials')


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='tutorial-detail', lookup_field='slug'
    )

    class Meta:
        model = Tutorial
        fields = ('name', 'slug', 'homepage_url', 'summary',
                  'url',)
        lookup_field = 'slug'
