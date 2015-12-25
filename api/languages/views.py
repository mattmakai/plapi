from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import render
from django.template.defaultfilters import slugify
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from taggit.models import Tag, TaggedItem

from .models import Language, Library, Tutorial
from .serializers import (LanguageSerializer, LibrarySerializer,
                         TutorialSerializer, )


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'libraries': reverse('libraries', request=request, format=format),
        'programming-languages': reverse('programming-languages',
                                         request=request, format=format),
        'tutorials': reverse('tutorials', request=request, format=format),
    })


class LanguageList(APIView):
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Language.objects.filter(is_visible=True)
        year_gte = self.request.query_params.get('year-gte', None)
        if year_gte is not None:
            queryset = queryset.filter(year_appeared__gte=year_gte)
        year_lte = self.request.query_params.get('year-lte', None)
        if year_lte is not None:
            queryset = queryset.filter(year_appeared__lte=year_lte)
        return queryset

    def get(self, request, format=None):
        languages = self.get_queryset().order_by('name')
        serializer = LanguageSerializer(languages, many=True,
                                        context={'request': request})
        return Response(serializer.data)


class LanguageDetail(APIView):
    def get_object(self, slug):
        try:
            language = Language.objects.filter(slug=slug,
                                               is_visible=True).first()
        except Language.DoesNotExist:
            raise Http404
        if language is None:
            raise Http404
        return language

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


class LibraryList(APIView):
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Library.objects.filter(is_visible=True)
        tags = self.request.query_params.get('tags', None)
        if tags is not None:
            tags_list = tags.strip().split(',')
            tags = Tag.objects.filter(name__in=tags_list)
            if not tags:
                return None
            library_type = ContentType.objects.get(app_label="languages",
                                                   model="library")
            object_ids = TaggedItem.objects.filter(content_type=library_type,
                                                   tag_id__in=tags).\
                                                   distinct('object_id').\
                                                   values_list('object_id',
                                                               flat=True)
            queryset = queryset.filter(pk__in=object_ids)
        return queryset

    def get(self, request, format=None):
        libraries = self.get_queryset()
        if libraries is not None:
            libraries.order_by('name')
            serializer = LibrarySerializer(libraries, many=True,
                                           context={'request': request})
            return Response(serializer.data)
        return Response([])


class LibraryDetail(APIView):
    def get_object(self, slug):
        try:
            library = Library.objects.filter(slug=slug,
                                             is_visible=True).first()
        except Library.DoesNotExist:
            raise Http404
        if library is None:
            raise Http404
        return library

    def get(self, request, slug, format=None):
        library = self.get_object(slug)
        serializer = LibrarySerializer(tutorial,
                                        context={'request': request})
        return Response(serializer.data)


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
            tutorial = Tutorial.objects.filter(slug=slug,
                                               is_visible=True).first()
        except Tutorial.DoesNotExist:
            raise Http404
        if tutorial is None:
            raise Http404
        return tutorial

    def get(self, request, slug, format=None):
        tutorial = self.get_object(slug)
        serializer = TutorialSerializer(tutorial,
                                        context={'request': request})
        return Response(serializer.data)

