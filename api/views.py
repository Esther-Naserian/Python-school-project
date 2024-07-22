from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classroom.models import Classroom
from classperiod.models import Classperiod
from course.models import Course
from .serializers import StudentSerializers
from .serializers import TeacherSerializer
from .serializers import ClassroomSerializer
from .serializers import ClassperiodSerializer
from .serializers import CourseSerializer
from rest_framework.response import Response

# Create your views here


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, data=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = teacher.objects.get(id=id)
        serializer = TeacherSerializer(Teacher)
        return Response(serializer.data)
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(Teacher, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, data=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        Teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)



class ClassroomListView(APIView):
    def get(self, request):
        classrooms = classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassroomSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ClassroomDetailView(APIView):
    def get(self,request,id):
        classroom = classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, data=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
          
class CourseDetailView(APIView):
    def get(self,request,id):
        course = course.objects.get(id=id)
        serializer = CourseSerializerSerializer(student)
        return Response(serializer.data)
    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, data=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




class ClassperiodListView(APIView):
    def get(self, request):
        classperiod = Classperiod.objects.all()
        serializer = ClassperiodSerializer(classperiod, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassperiodSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ClassperiodDetailView(APIView):
    def get(self,request,id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod)
        return Response(serializer.data)
    def put(self, request, id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, data=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classperiod = Classperiod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)