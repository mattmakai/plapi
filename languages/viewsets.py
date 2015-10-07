from rest_framework import viewsets

from .models import Library, ProgrammingLanguage, Tutorial
from .serializers import (LibrarySerializer, ProgrammingLanguageSerializer,
                          TutorialSerializer)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.filter(is_visible=True)
    serializer_class = LibrarySerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.filter(is_visible=True)
    serializer_class = ProgrammingLanguageSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.filter(is_visible=True)
    serializer_class = TutorialSerializer
