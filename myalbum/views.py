#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
import getUrl
from .forms import siteForm  # form for get site

defaultUrl = 'http://www.meizitu.com'

# Create your views here.

def myalbum_simple(request):
    photo_list = getUrl.getImgList('meizitu.com')
    return render(request, u'myalbum/myalbum.html', {'photo_list': photo_list})

def myalbum(request, url = defaultUrl):
    if request.method == 'POST':        # when POST
        form = siteForm(request.POST)

        if form.is_valid():
            site = form.cleaned_data['site']
            photo_list = getUrl.getImgList(site)
            return render(request, u'myalbum/myalbum.html', {'form': form,
                                                     'photo_list': photo_list,
                                                     'site': site})
        else:   # when POST is invalid
            form = siteForm()
            site = defaultUrl
            photo_list = getUrl.getImgList(site) 
            return render(request, u'myalbum/myalbum.html', {'form': form,
                                                     'photo_list': photo_list,
                                                     'site': site})
            
    else:       # when not POST , just by /url/(.+?)
        form = siteForm()
        site = url
        photo_list = getUrl.getImgList(site) 
    return render(request, u'myalbum/myalbum.html', {'form': form,
                                             'photo_list': photo_list,
                                             'site': site})
