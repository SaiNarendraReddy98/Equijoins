from django.shortcuts import render
from app.models import *

# Create your views here.

def equijoins(request):
    Empobj = Emp.objects.select_related('deptno').all()
    Empobj = Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    Empobj = Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    Empobj = Emp.objects.select_related('deptno').filter(deptno__dloc='Boston')
    Empobj = Emp.objects.select_related('deptno').filter(sal__gt=3000)
    Empobj = Emp.objects.select_related('deptno').filter(comm__isnull=False)
    

    d={'Empobj':Empobj}

    return render(request,'equijoins.html',d)


