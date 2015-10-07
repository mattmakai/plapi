from rest_framework import reverse, serializers

from .models import Library, ProgrammingLanguage, Tutorial

"""
class ProgrammingLanguageHyperlink(serializers.HyperlinkedRelatedField):
    view_name = 'programminglanguage-detail'
    queryset = ProgrammingLanguage.objects.filter(is_visible=True)

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'slug': obj.slug,
        }
        return reverse(view_name, url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
           'slug': view_kwargs['slug'],
        }
        return self.get_queryset().get(**lookup_kwargs)



class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('name', 'slug', 'language', 'summary', 'url',)
        lookup_field = 'slug'
"""

class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ('name', 'slug', 'homepage_url', 'summary',) 

"""
class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('name', 'slug', 'homepage_url', 'language', 'summary',
                  'url',)
        lookup_field = 'slug'
"""
