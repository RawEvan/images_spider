#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import siteForm  # form for getting site
import getUrl
import json

defaultUrl = 'http://www.tuchong.com'

# Create your views here.


def myalbum(request, url=defaultUrl):
    ''' here use two ways to get post infomation: POST or urls.py
    it'll be change in the future...
    the photo_list is the same as the urlInfoList, the name just make it more like an album...
    '''
    if request.method == 'POST':        # when POST
        form = siteForm(request.POST)

        if form.is_valid():
            site = form.cleaned_data['site']
        else:   # when POST is invalid
            site = defaultUrl

    else:       # when not POST , just get url by GET method with '/url/(.+?)'
        form = siteForm()
        site = url
    fixed_site, photo_list = getUrl.getImgList(site)
    return render(request, u'myalbum/myalbum.html', {'form': form,
                                                     'photo_list': photo_list,
                                                     'site': fixed_site})
