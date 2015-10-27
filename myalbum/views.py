#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
import getUrl
from .forms import siteForm  # form for get site

# Create your views here.

def myalbum_simple(request):
    photo_list = getUrl.getImgList('meizitu.com')
    return render(request, u'myalbum.html', {'photo_list': photo_list})

def myalbum(request):
    if request.method == 'POST':        # when POST
        form = siteForm(request.POST)

        if form.is_valid():
            site = form.cleaned_data['site']
            photo_list = getUrl.getImgList(site)
            return render(request, u'myalbum.html', {'form': form,
                                                     'photo_list': photo_list,
                                                     'site': site})
    else :          # when not POST
        form = siteForm()
        site = 'http://www.meizitu.com'
        photo_list = getUrl.getImgList(site)
    return render(request, u'myalbum.html', {'form': form,
                                             'photo_list': photo_list,
                                             'site': site})

def myalbum_geturl(request, url):
    form = siteForm()
    photo_list = getUrl.getImgList(url) 
    return render(request, u'myalbum.html', {'form': form,
                                             'photo_list': photo_list,
                                             'site': url})
