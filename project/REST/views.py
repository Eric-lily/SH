from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView,Response
# Create your views here.
from common.models import User,Book,Student
from REST.serializers import UserSerializer,BookSerializer
from django.views import View
from REST.serializers import StudentSerializer
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    serializer_class = BookSerializer

class StudentView(APIView):
    def post(self,request):
        s_name = request.POST.get('s_name')
        s_age = request.POST.get('s_age')
        student = Student()
        student.s_name = s_name
        student.s_age = s_age
        student.save()
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)

    def get(self,request):
        students = Student.objects.all()
        students_serializers = StudentSerializer(students,many=True)
        return Response(students_serializers.data)

    def put(self,request,nid):
        stu_obj = Student.objects.get(s_age=nid)
        validated_data = StudentSerializer(data=request.data,instance=stu_obj)
        if validated_data.is_valid():
            validated_data.save()
            return Response(validated_data.data)
        else:
            return Response(validated_data.errors)

    def delete(self,request,nid):
        Student.objects.get(s_age=nid).delete()
        return Response('删除成功')

# class StudentView(View):
#     def post(self,request):
#         data = JSONParser().parse(request)
#         students_serializers = StudentSerializer(data=data)
#         if students_serializers.is_valid():
#             students_serializers.save()
#             return JsonResponse(students_serializers.data,status=201)
#         return JsonResponse(students_serializers.errors,status=400)

        

    