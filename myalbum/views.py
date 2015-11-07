#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
import getUrl
from .forms import siteForm  # form for get site
import storage
import json

defaultUrl = 'http://www.tuchong.com'

# Create your views here.

def myalbum_simple(request):
    photo_list = getUrl.getImgList(defaultUrl)  # it's the old way, now don't use getUrl.py
    return render(request, u'myalbum/myalbum.html', {'photo_list': photo_list})

def myalbum(request, url = defaultUrl):
    ''' here use two ways to get post infomation: POST or urls.py
    it'll be change in the future...
    the photo_list is the same as the urlInfoList, the name just make it more like an album...
    '''
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

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def storeImages(request):
    if request.method == 'POST':
        urlDictList = json.loads(request.POST['urlDictList'])
        for imgInfo in urlDictList:
            storage.storeImage(imgInfo)
        return '200-ok, all images storaged'
    else:
        return HttpResponse(u'<htm><body>store images</body></html>')

def storeImagesByGet(request, url):
    storage.storeImage(url)
    return '200-ok'
