from django.contrib import admin

from .models import (Concept, Implementation, ProgrammingLanguage, Paradigm,
                     Tutorial,)


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Implementation)
class ImplementationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Paradigm)
class ParadigmAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')

