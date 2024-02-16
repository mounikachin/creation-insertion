from typing import Any
from django.db import models

# Create your models here.
class Emp(models.Model):
    deptno=models.ForeignKey('Dept',on_delete=models.CASCADE)
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    job=models.CharField(max_length=100)
    
     
    def __str__(self):
       return self.ename
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return self.dname
        