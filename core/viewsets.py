from rest_framework import viewsets

from core.models import (ProgrammingLanguage, Paradigm,)
from .serializers import (ProgrammingLanguageSerializer,
                          ParadigmSerializer,)


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer


class ParadigmViewSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
