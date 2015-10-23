#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
import getUrl
from .forms import siteForm  # form for get site

# Create your views here.

def myalbum_old(request):
##    photo_list = [u"http://pic.meizitu.com/wp-content/uploads/2015a/10/27/01.jpg",
##                  u"http://pic.meizitu.com/wp-content/uploads/2015a/10/24/01.jpg"]
    photo_list = getUrl.getImgList('http://meizitu.com')
    return render(request, u'myalbum.html', {'photo_list': photo_list})

def addHead(site):
    if 'static' not in site:
        if 'www.' not in site:
            site = 'www.' + site
            if 'http://' not in site:
                site = 'http://' + site
    return site

def myalbum(request):
    if request.method == 'POST':        # when POST
        form = siteForm(request.POST)

        if form.is_valid():
            site = form.cleaned_data['site']
            site = addHead(site)  # add http head if don't have
            photo_list = getUrl.getImgList(site)
            return render(request, u'myalbum.html', {'form': form, 'photo_list': photo_list})
    else :          # when not POST
        form = siteForm()
        photo_list = getUrl.getImgList('http://www.meizitu.com')
    return render(request, u'myalbum.html', {'form': form, 'photo_list': photo_list})
