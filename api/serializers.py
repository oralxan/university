from rest_framework .serializers import ModelSerializer

from faculty_fields.models import(
    Tuition_language,
    Education_form,
    Subject
)
from faculty.models import Faculty
from universities.models import University
class Tuition_languageSerializer(ModelSerializer):
    class Meta:
        model= Tuition_language
        fields = '__all__'
class Education_formSer(ModelSerializer):
    class Meta:
        model= Education_form
        fields = '__all__'
class SubjectSer(ModelSerializer):
    class Meta:
        model= Subject
        fields = '__all__'
class FacultySerializer(ModelSerializer):
    class Meta:
        model= Faculty
        fields = '__all__'
class UniversitySer(ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
