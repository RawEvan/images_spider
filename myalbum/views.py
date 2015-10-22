#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.

def myalbum(request):
    photo_list = [u"http://pic.meizitu.com/wp-content/uploads/2015a/10/27/01.jpg",
                  u"http://pic.meizitu.com/wp-content/uploads/2015a/10/24/01.jpg"]
    return render(request, u'myalbum.html', {'photo_list': photo_list})
