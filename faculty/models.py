from django.db.models import *

# Create your models here.
from universities.models import University
from faculty_fields.models import (
    Tuition_language,
    Education_form,
    Subject
)

class Faculty(Model):
    university = ForeignKey(
        University,
        verbose_name='University',
        on_delete=CASCADE
    )
    name = CharField(
        'Faculty Name',
        max_length=256
    )
    tuition_languages = ManyToManyField(
        Tuition_language,
        verbose_name='Tuition Languages'
    )
    education_forms = ManyToManyField(
        Education_form,
        verbose_name='Education Forms'
    )
    acceptance = PositiveSmallIntegerField(
        'Acceptance Number'
    )
    grant = DecimalField(
        'Grant Score',
        decimal_places=1,
        blank=True,
        null=True,
        max_digits=4
    )
    contract = DecimalField(
        'Contract Score',
        decimal_places=1,
        blank=True,
        null=True,
        max_digits=4
    )
    first_subject = OneToOneField(
        Subject,
        verbose_name='First Subject',
        on_delete=CASCADE,
        related_name='first_subject_relation'
)
    second_subject = OneToOneField(
        Subject,
        verbose_name='Second Subject',
        on_delete=CASCADE,
        related_name='second_subject_relation'
)
    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
