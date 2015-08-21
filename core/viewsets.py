from rest_framework import viewsets

from core.models import ProgrammingLanguage
from .serializers import ProgrammingLanguageSerializer


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer

