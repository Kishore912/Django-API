from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Salary = models.IntegerField(max_length=50)
    native = models.CharField(max_length=50)

    def __str__(self):
        return self.name



