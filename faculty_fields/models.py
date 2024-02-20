from django.db.models import *
class Tuition_language(Model):
    language = CharField(
        'language',
        max_length=32
    )
    def __str__(self):
        return f'{self.language}'
    class Meta:
        verbose_name = 'Tuition_language'
        verbose_name_plural = 'Tuition_languages'
class Education_form(Model):
    eduname = CharField(
        'eduname',
        max_length=32
    )
    def __str__(self):
        return f'{self.eduname}'
    class Meta:
        verbose_name = 'Education_form'
        verbose_name_plural = 'Education_forms'
class Subject(Model):
    subname = CharField(
        'subname',
        max_length=32
    )
    def __str__(self):
        return f'{self.subname}'
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'



