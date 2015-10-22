#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.

def myalbum(request):
    return render(request, u'myalbum.html')
