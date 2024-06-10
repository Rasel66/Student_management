from django.db import models

class Student(models.Model):
    roll = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    result = models.FloatField()

    def __str__(self):
        return f"Student: {self.name}"
# Create your models here.
