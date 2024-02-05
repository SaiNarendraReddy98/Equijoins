from django.shortcuts import render
from app.models import *
from django.db.models import Q

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


def emp_mgr_dept(request):

    Emdobj = Emp.objects.select_related('deptno','mgr').all()
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(ename='Jones')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(sal__gt=2500)
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(sal__lt=2500)
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(ename='Jones',mgr__ename='King')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='Boston')
    Emdobj = Emp.objects.select_related('deptno','mgr').all()[:5:]
    Emdobj = Emp.objects.select_related('deptno','mgr').all()[6:10:]
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(ename__startswith='J')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='s') | Q(deptno__dname='Operations'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(hiredate__month__gt=1,hiredate__month__lt=3)
    Emdobj = Emp.objects.select_related('deptno','mgr').all()
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(comm__gt=1400,deptno__dname='sales')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='A') | Q(deptno__dname='Research'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__endswith='S') | Q(deptno__dname='Dallas'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(job='Manager')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='s') | Q(deptno__dname='Operations'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__endswith='t') | Q(deptno__dname='Accounting'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='J') | Q(ename__endswith='T'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(deptno__in=(10,20))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(job__in=('Manager','president'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(ename__contains='e')
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='L') | Q(deptno__dname='Sales'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='k') | Q(deptno__dloc='Boston'))
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='Accounting') | Q(deptno__dname='Dallas'))
    Emdobj = Emp.objects.select_related('deptno','mgr').all()[::-1]
    Emdobj = Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='New York')

    d = {'Emdobj':Emdobj}
    return render(request,'emp_mgr_dept.html',d)



def emp_salgrade(request):
    # retreving the data of Employee with they salgrade
    EO = Emp.objects.all()
    SO = SalGrade.objects.all()

    # retreving only particular grade
    SO = SalGrade.objects.filter(grade=3)
    EO = Emp.objects.filter(sal__range=(SO[0].lowsal,SO[0].highsal))

    #retriving the data of morethan 2 grades
    SO = SalGrade.objects.filter(grade__in=(1,2,5,4))
    EO = Emp.objects.none()
    for sgo in SO:
        EO = EO | Emp.objects.filter(sal__range=(sgo.lowsal,sgo.highsal))


    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)


    




