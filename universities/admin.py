from django.contrib.admin import *
from .models import University
@register(University)
class UniversityAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering= ('name',)


# Register your models here.

