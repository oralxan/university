from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from .serializers import(
    Tuition_languageSerializer,
    Education_formSer,
    SubjectSer,
    FacultySerializer,
    UniversitySer

)
from faculty_fields.models import (
    Tuition_language,
    Education_form,
    Subject
)
from faculty.models import Faculty
from universities.models import University
##########  importer ###########
#tuition lan#
class Tuition_languageSerializerList(APIView):
    def get(self,request,format=None):
        queryset = Tuition_language.objects.all()
        serializer = Tuition_languageSerializer(queryset,many= True)
        return Response(
            serializer.data,
            status = HTTP_200_OK
        )
    def post(self, request, format = None):
        serializer = Tuition_languageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = HTTP_400_BAD_REQUEST
        )
class Tuition_languageSerializerDetail(APIView):

    def get_object(self,pk):
        try:
            return Tuition_language.objects.get(pk=pk)
        except Tuition_language.DoesNotExist:
            return Response(
                'Not found'
            )
    def get(self, request,pk, format=None):
        queryset = self.get_object(pk)
        serializer =Tuition_languageSerializer(queryset)
        
        return Response(
            serializer.data,
            status = HTTP_200_OK
            )
    def put(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = Tuition_languageSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def patch(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = Tuition_languageSerializer(queryset, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def delete(self, request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(
            'delete',
            status = HTTP_204_NO_CONTENT
        )
################-------------------Education-------------------################




#eduction lan#
class Education_formSerList(APIView):
    def get(self,request,format=None):
        queryset = Education_form.objects.all()
        serializer = Education_formSer(queryset,many= True)
        return Response(
            serializer.data,
            status = HTTP_200_OK
        )
    def post(self, request, format = None):
        serializer = Education_formSer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = HTTP_400_BAD_REQUEST
        )
class Education_formDetail(APIView):

    def get_object(self,pk):
        try:
            return Education_form.objects.get(pk=pk)
        except Education_form.DoesNotExist:
            return Response(
                'Not found'
            )
    def get(self, request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = Education_formSer(queryset)
        
        return Response(
            serializer.data,
            status = HTTP_200_OK
            )
    def put(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = Education_formSer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def patch(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = Education_formSer(queryset, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def delete(self, request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(
            'delete',
            status = HTTP_204_NO_CONTENT
        )
################-------------------Subject-------------------################
#SubjectSer#
class SubjectSerList(APIView):
    def get(self,request,format=None):
        queryset = Subject.objects.all()
        serializer = SubjectSer(queryset,many= True)
        return Response(
            serializer.data,
            status = HTTP_200_OK
        )
    def post(self, request, format = None):
        serializer = SubjectSer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = HTTP_400_BAD_REQUEST
        )
class SubjectSerDetail(APIView):

    def get_object(self,pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response(
                'Not found'
            )
    def get(self, request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = SubjectSer(queryset)
        
        return Response(
            serializer.data,
            status = HTTP_200_OK
            )
    def put(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = SubjectSer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def patch(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = SubjectSer(queryset, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def delete(self, request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(
            'delete',
            status = HTTP_204_NO_CONTENT
        )
################-------------------Faculty-------------------################
#Faculty#
class FacultySerializerList(APIView):
    def get(self,request,format=None):
        queryset = Faculty.objects.all()
        serializer = FacultySerializer(queryset,many= True)
        return Response(
            serializer.data,
            status = HTTP_200_OK
        )
    def post(self, request, format = None):
        serializer = FacultySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = HTTP_400_BAD_REQUEST
        )
class FacultySerializerDetail(APIView):

    def get_object(self,pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return Response(
                'Not found'
            )
    def get(self, request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = FacultySerializer(queryset)
        
        return Response(
            serializer.data,
            status = HTTP_200_OK
            )
    def put(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = FacultySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def patch(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = FacultySerializerDetail(queryset, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def delete(self, request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(
            'delete',
            status = HTTP_204_NO_CONTENT
        )
################-----------------University---------------------################




#University#
class UniversitySerList(APIView):
    def get(self,request,format=None):
        queryset = University.objects.all()
        serializer = UniversitySer(queryset,many= True)
        return Response(
            serializer.data,
            status = HTTP_200_OK
        )
    def post(self, request, format = None):
        serializer = UniversitySer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = HTTP_400_BAD_REQUEST
        )
class UniversityDetail(APIView):

    def get_object(self,pk):
        try:
            return University.objects.get(pk=pk)
        except University.DoesNotExist:
            return Response(
                'Not found'
            )
    def get(self, request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = UniversitySer(queryset)
        
        return Response(
            serializer.data,
            status = HTTP_200_OK
            )
    def put(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = UniversitySer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def patch(self, request,pk ,format =None):
        queryset = self.get_object(pk)
        serializer = UniversitySer(queryset, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status = HTTP_406_NOT_ACCEPTABLE
        )
    def delete(self, request,pk,format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(
            'delete',
            status = HTTP_204_NO_CONTENT
        )