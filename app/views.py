from django.shortcuts import render
from app.models import *

# Create your views here.

def equijoins(request):
    Empobj = Emp.objects.select_related('deptno').all()
    Empobj = Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    Empobj = Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    Empobj = Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    Empobj = Emp.objects.select_related('deptno').filter(deptno__dloc='Boston')
    Empobj = Emp.objects.select_related('deptno').filter(sal__gt=3000)
    Empobj = Emp.objects.select_related('deptno').filter(comm__isnull=False)
    Empobj = Emp.objects.select_related('deptno').all()
    Empobj = Emp.objects.select_related('deptno').filter(deptno__dloc='Accounting')
    Empobj = Emp.objects.select_related('deptno').filter(deptno=10)
    Empobj = Emp.objects.select_related('deptno').filter(deptno__dloc='Dallas')
    Empobj = Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    Empobj = Emp.objects.select_related('deptno').filter(ename='King')
    Empobj = Emp.objects.select_related('deptno').filter(sal__lt=3000)
    Empobj = Emp.objects.select_related('deptno').filter(comm__isnull=True)    

    d = {'Empobj':Empobj}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    Emobj = Emp.objects.select_related('mgr').all()
    Emobj = Emp.objects.select_related('mgr').filter(sal__gte=2500)
    Emobj = Emp.objects.select_related('mgr').filter(mgr__ename='Blake',sal__lte=1300)
    Emobj = Emp.objects.select_related('mgr').filter(sal__lte=2000)
    Emobj = Emp.objects.select_related('mgr').filter(hiredate__year=2023)
    Emobj = Emp.objects.select_related('mgr').filter(sal=5000)
    Emobj = Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    Emobj = Emp.objects.select_related('mgr').all()[1:6:]
    Emobj = Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    Emobj = Emp.objects.select_related('mgr').filter(sal__lt=2500)
    Emobj = Emp.objects.select_related('mgr').filter(comm__isnull=True)
    Emobj = Emp.objects.select_related('mgr').filter(comm__isnull=False)
    Emobj = Emp.objects.select_related('mgr').filter(deptno=10)
    Emobj = Emp.objects.select_related('mgr').all()[6:10:]
    Emobj = Emp.objects.select_related('mgr').filter(hiredate__year=2023,sal__lt=2500)
    


    d = {'Emobj':Emobj}
    return render(request,'selfjoins.html',d)