from django.urls import path
from .views import(
    Tuition_languageSerializerList,
    Tuition_languageSerializerDetail,
    Education_formSerList,
    Education_formDetail,
    SubjectSerDetail,
    SubjectSerList,
    FacultySerializerDetail,
    FacultySerializerList,
    UniversityDetail,
    UniversitySerList
)
urlpatterns = [
    path('tuition-lan/', Tuition_languageSerializerList.as_view(),name='tut'),
    path('tuition-lan/<int:pk>/',Tuition_languageSerializerDetail.as_view()),
    path('Edulist/', Education_formSerList.as_view(),name='edulist'),
    path('Edudetail/<int:pk>/',Education_formDetail.as_view()),
    path('sublist/',SubjectSerList.as_view(), name='sublist'),
    path('subdetail/<int:pk>/',SubjectSerDetail.as_view()),
    path('facultylist/',FacultySerializerList.as_view()),
    path('facultydetail/<int:pk>/',FacultySerializerDetail.as_view()),
    path('univer/',UniversitySerList.as_view(),name='univer'),
    path('univerdetail/<int:pk>/',UniversityDetail.as_view())

]