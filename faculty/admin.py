from django.contrib.admin import *
from .models import Faculty
@register(Faculty)
class FacultyAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ('id',)

# Register your models here.
