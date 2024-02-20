from django.contrib.admin import *
from .models import (
    Tuition_language,
    Education_form,
    Subject
)
@register(Tuition_language)
class Tuition_languageAdmin(ModelAdmin):
    list_display= ('id','language')
    list_display_links = ('id','language')

@register(Education_form)
class Education_formAdmin(ModelAdmin):
    list_display= ('id','eduname')
    list_display_links = ('id','eduname')
@register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display= ('id','subname')
    list_display_links = ('id','subname')