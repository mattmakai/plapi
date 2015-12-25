from rest_framework import reverse, serializers
from rest_framework.serializers import HyperlinkedRelatedField

from .models import Library, Language, Tutorial


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='language-detail', lookup_field='slug'
    )
    tutorials = HyperlinkedRelatedField(many=True, read_only=True,
                                        view_name='tutorial-detail',
                                        lookup_field='slug')

    class Meta:
        model = Language
        fields = ('name', 'url', 'homepage_url', 'year_appeared', 'summary',
                  'tutorials')


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='library-detail', lookup_field='slug'
    )
    language = HyperlinkedRelatedField(many=False, read_only=True,
                                        view_name='language-detail',
                                        lookup_field='slug')
    class Meta:
        model = Library
        fields = ('name', 'url', 'language', 'homepage_url', 'package_url',
                  'summary',)
        lookup_field = 'slug'


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='tutorial-detail', lookup_field='slug'
    )
    language = HyperlinkedRelatedField(many=False, read_only=True,
                                        view_name='language-detail',
                                        lookup_field='slug')

    class Meta:
        model = Tutorial
        fields = ('name', 'url', 'tutorial_url', 'summary', 'language')
        lookup_field = 'slug'

