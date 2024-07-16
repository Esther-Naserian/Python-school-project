from django.db import models

# Create your models here.
class  Teacher(models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    teacher_gender=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20)
    teacher_email=models.EmailField()
    teacher_specilization=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    year_of_birth=models.PositiveSmallIntegerField()
    

    def __str__(self):
        return f"{self.first_name} {self.teacher_specilization}"




   
   
