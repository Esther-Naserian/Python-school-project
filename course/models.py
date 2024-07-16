from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_description=models.CharField(max_length=20)
    course_capacity=models.PositiveSmallIntegerField()
    course_teacher_in_charge=models.CharField(max_length=20)
    course_student_enrolled=models.PositiveSmallIntegerField()
    course_start_time=models.CharField(max_length=20)
    course_assessment_method=models.CharField(max_length=20)


def __str__(self):
        return f"{self.course_name} {self.course_teacher_in_charge}"




    