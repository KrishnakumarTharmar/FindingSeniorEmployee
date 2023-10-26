from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    join_year = models.IntegerField()
    department = models.CharField(max_length=20)
