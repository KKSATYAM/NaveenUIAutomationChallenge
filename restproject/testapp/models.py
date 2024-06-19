from django.db import models

class EmployeeModel(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=6)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=6)

