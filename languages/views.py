from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Language, Tutorial
from .serializers import LanguageSerializer, TutorialSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'programming-languages': reverse('programming-languages',
                                         request=request, format=format),
    })


class LanguageList(APIView):
    queryset = Language.objects.filter(is_visible=True)

    def get(self, request, format=None):
        languages = Language.objects.filter(is_visible=True)
        serializer = LanguageSerializer(languages, many=True,
                                        context={'request': request})
        return Response(serializer.data)


class LanguageDetail(APIView):
    def get_object(self, slug):
        try:
            return Language.objects.filter(slug=slug).first()
        except Language.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        language = self.get_object(slug)
        serializer = LanguageSerializer(language,
                                        context={'request': request})
        return Response(serializer.data)


class TutorialDetail(APIView):
    def get_object(self, slug):
        try:
            return Tutorial.objects.filter(slug=slug).first()
        except Tutorial.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        tutorial = self.get_object(slug)
        serializer = TutorialSerializer(tutorial,
                                        context={'request': request})
        return Response(serializer.data)

