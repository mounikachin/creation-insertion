from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_dept(request):
    dobj=Dept.objects.get_or_create(deptno=1,dname='ACCOUNTING',dloc='BANGLORE')[0]
    dobj.save()
    dobj1=Dept.objects.get_or_create(deptno=2,dname='RESEARCH',dloc='HYD')[0]
    dobj1.save()
    dobj2=Dept.objects.get_or_create(deptno=3,dname='IT',dloc='CHENNAI')[0]
    dobj2.save()
    return HttpResponse('data is inserted')
def insert_emp(request):
    deobj=Dept.objects.get(deptno=1)
    eobj=Emp.objects.get_or_create(empno=1,ename='mouni',esal=10000,job='teacher',deptno=deobj)[0]
    eobj.save()
    deobj=Dept.objects.get(deptno=2)
    eobj1=Emp.objects.get_or_create(empno=2,ename='Ram',esal=20000,job='developer',deptno=deobj)[0]
    eobj1.save()
    deobj=Dept.objects.get(deptno=3)
    eobj2=Emp.objects.get_or_create(empno=3,ename='Ram',esal=20000,job='developer',deptno=deobj)[0]
    eobj2.save()
    return HttpResponse('hgfhgd')