# -*- coding:utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
##    return HttpResponse(u"welcome!")

##    return render(request, 'home.html')

    string = [u'how are you', u'how old are you']
    string1 = u'string11'
    return render(request, 'home.html', {'string': string, 'string1': string1})
