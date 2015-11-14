# -*- coding: utf-8 -*-
'''
this file connects the spider and the view which
change class to dict or list,
this is unnecessary when 'mySpider.py' was changed to
return a list of Dict
----
use this again to connect to storage and keep server files seperated
'''
import re
import urllib2
import urllib
import mySpider
import storage
import json
from myalbum.models import imgstorage
defaultUrl = 'image.baidu.com'

def getImgList_old(url = defaultUrl):   # old function
    html = getHtml(url)
##    re2=r'meizitu.com/.+\.jpg'
    re2 = '(?<=src=\").+?(?<!limg)\.jpg(?=\")'      # limg means it's a small image
    imglist = re.findall(re2, html)
    return imglist

def getImgList(url = defaultUrl):
    try:
        urlDictList = mySpider.getImg(url)
    except:
        urlDictList = [{'href': 'evandjango.sinaapp.com',
                        'src': '/static/images/noimage.jpg',
                        'description': 'no description'}]
    storageUrl = u'http://6.evandjango.sinaapp.com/storageGet/'
    '''
    srcList = []
    for each in urlDictList:
        srcList.append(each['src'])
    jsonSrcList = json.dumps(srcList)
    data =  {'urlDictList': jsonSrcList}
    encodeData = urllib.urlencode(data)
    req = urllib2.Request(storageUrl, encodeData)
    response = urllib2.urlopen(req)
    '''
    for each in urlDictList:
        try:
            response = urllib2.urlopen(storageUrl + each['src'])    # store images to storage
        except:
            pass    # solve this later
        
    # replace original_url with storage_url
    for each in urlDictList:
        try:
            each['src'] = (imgstorage.objects.get(original_url = each['src'])).storage_url
        except:
            pass    # solve this later
    return urlDictList
