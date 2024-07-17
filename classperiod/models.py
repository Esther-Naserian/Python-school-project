from django.db import models
from course.models import Course


# Create your models here.
class Classperiod(models.Model):
    class_start_time = models.DurationField()
    class_end_time = models.DurationField()
    class_courses_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    classroom_class = models.OneToOneField(Classroom, on_delete=models.CASCADE, related_name='class_period')
    day_of_the_week = models.ManyToManyField(DayOfWeek, related_name='class_periods')

    def __str__(self):
        return f"{self.class_start_time} - {self.class_end_time}"