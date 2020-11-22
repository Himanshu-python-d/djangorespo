from django.shortcuts import render
from testapp.models import *
# Create your views here.

def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dic={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dic)

def punejobs1(request):
    jobs_list=punejobs.objects.order_by('date')
    my_dic={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dic)

def chennaijobs1(request):
    jobs_list=chennaijobs.objects.order_by('date')
    my_dic={'jobs_list':jobs_list}
    return render(request,'testapp/chennaijobs.html',context=my_dic)
