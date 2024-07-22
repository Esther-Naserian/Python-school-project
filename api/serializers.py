from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classperiod.models import Classperiod
from classroom.models import Classroom

class StudentSerializers(serializers.ModelSerializer):
   class Meta:
     model = Student
     fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields = "__all__"from django.db import models
from .models import  Classroom
# Create your models here.
# Create your models here.

class ClassPeriod(models.Model):
    start_time =models.DateField()
    end_time =models.DateField()
    course =models.CharField(max_length=50)
    classroom =models.CharField(max_length=150)
    day_of_the_week =models.CharField(max_length=7)



    def __str__(self):
        return self.classroom


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
    fields = "__all__"
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
    model= Classroom
    fields = "__all__"
class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classperiod
        fields ="__all__"
    