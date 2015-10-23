from rest_framework import reverse, serializers

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
        view_name='language_detail',
        lookup_field='slug'
    )

    class Meta:
        model = Language
        fields = ('name', 'url', 'homepage_url', 'summary',)

"""
class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('name', 'slug', 'homepage_url', 'language', 'summary',
                  'url',)
        lookup_field = 'slug'
"""
