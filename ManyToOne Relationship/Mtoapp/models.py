from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.IntegerField()
    def __str__(self):
        return self.name
class Course(models.Model):
    Student = ManyToManyField(Student)
    cname = models.CharField(max_length=100)
    cost = models.IntegerField()
    def __str__(self):
        return self.cname
