from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    student_email=models.EmailField(max_length=20)
    student_nationality=models.CharField(max_length=20)
    student_date_of_birth=models.DateField()
    student_code=models.PositiveSmallIntegerField()
    
def __str__(self):
        return f"{self.first_name} {self.student_code}"

