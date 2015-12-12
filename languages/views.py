from django.shortcuts import render
from django.template.defaultfilters import slugify
from rest_framework import status
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
        'tutorials': reverse('tutorials', request=request, format=format),
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

    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data,
                                        context={'request': request})
        if serializer.is_valid():
            slug = slugify(serializer.validated_data['name'])
            serializer.save(slug=slug, is_visible=False)
            language = Language.objects.filter(slug=slug).first()
            serializer = LanguageSerializer(language,
                                            context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class TutorialList(APIView):
    queryset = Tutorial.objects.filter(is_visible=True)

    def get(self, request, format=None):
        tutorials = Tutorial.objects.filter(is_visible=True)
        serializer = TutorialSerializer(tutorials, many=True,
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

