from django.db import models

# Create your models here.
class Classperiod(models.Model):
    class_start_time=models.DurationField()
    class_end_time=models.DurationField()
    class_courses_course=models.CharField(max_length=20)
    classroom_class=models.CharField(max_length=20)
    day_of_the_week=models.CharField(max_length=20)

def __str__(self):
        return f"{self.class_start_time} {self.class_end_time}"
