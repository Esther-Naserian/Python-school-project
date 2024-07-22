from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_name=models.CharField(max_length=200)
    class_capacity=models.PositiveSmallIntegerField()
    class_teacher_in_charge=models.CharField(max_length=20)
    class_number_of_groups=models.PositiveSmallIntegerField()
    class_courses=models.PositiveSmallIntegerField()
    class_description=models.PositiveSmallIntegerField()


    def __str__(self):
        return f"{self.class_name}"
from django.db import models
