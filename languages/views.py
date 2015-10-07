from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import ProgrammingLanguage
from .serializers import ProgrammingLanguageSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'programming-languages': reverse('programming-languages',
                                         request=request, format=format),
        #'snippets': reverse('snippet-list', request=request, format=format)
    })


class ProgrammingLanguageList(APIView):
    queryset = ProgrammingLanguage.objects.filter(is_visible=True)

    def get(self, request, format=None):
        languages = ProgrammingLanguage.objects.filter(is_visible=True)
        serializer = ProgrammingLanguageSerializer(languages, many=True)
        return Response(serializer.data)
