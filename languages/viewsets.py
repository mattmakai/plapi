from rest_framework import viewsets
from rest_framework.response import Response

from .models import Library, ProgrammingLanguage, Tutorial
from .serializers import (LibrarySerializer, ProgrammingLanguageSerializer,
                          TutorialSerializer)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.filter(is_visible=True)
    serializer_class = LibrarySerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, slug=None):
        languages = ProgrammingLanguage.objects.filter(slug=slug)
        if len(languages) == 1:
            language = languages[0]
        print language
        serializer = ProgrammingLanguageSerializer(language)
        return Response(serializer.data)


    queryset = ProgrammingLanguage.objects.filter(is_visible=True)
    serializer_class = ProgrammingLanguageSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.filter(is_visible=True)
    serializer_class = TutorialSerializer
