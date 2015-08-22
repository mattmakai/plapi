from django.contrib import admin

from .models import (Library, ProgrammingLanguage, Paradigm, Tutorial,)


admin.site.register(Library)

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')


admin.site.register(Paradigm)
admin.site.register(Tutorial)
