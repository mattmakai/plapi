from django.contrib import admin

from .models import Library, ProgrammingLanguage, Tutorial


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')
