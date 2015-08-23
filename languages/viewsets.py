from rest_framework import viewsets

from .models import (Concept, Implementation, ProgrammingLanguage,
                     Paradigm, Tutorial)
from .serializers import (ConceptSerializer, ImplementationSerializer,
                          ProgrammingLanguageSerializer, ParadigmSerializer,
                          TutorialSerializer)


class ConceptViewSet(viewsets.ModelViewSet):
    queryset = Concept.objects.filter(is_visible=True)
    serializer_class = ConceptSerializer


class ImplementationViewSet(viewsets.ModelViewSet):
    queryset = Implementation.objects.filter(is_visible=True)
    serializer_class = ImplementationSerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.filter(is_visible=True)
    serializer_class = ProgrammingLanguageSerializer


class ParadigmViewSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.filter(is_visible=True)
    serializer_class = ParadigmSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.filter(is_visible=True)
    serializer_class = TutorialSerializer
