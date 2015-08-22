from rest_framework import viewsets

from core.models import (Library, ProgrammingLanguage, Paradigm, Tutorial)
from .serializers import (LibrarySerializer, ProgrammingLanguageSerializer,
                          ParadigmSerializer, TutorialSerializer)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.filter(is_visible=True)
    serializer_class = LibrarySerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.filter(is_visible=True)
    serializer_class = ProgrammingLanguageSerializer


class ParadigmViewSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.filter(is_visible=True)
    serializer_class = ParadigmSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.filter(is_visible=True)
    serializer_class = TutorialSerializer
