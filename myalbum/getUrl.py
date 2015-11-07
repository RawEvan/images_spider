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

defaultUrl = 'image.baidu.com'

def getImgList_old(url = defaultUrl):   # old function
    html = getHtml(url)
##    re2=r'meizitu.com/.+\.jpg'
    re2 = '(?<=src=\").+?(?<!limg)\.jpg(?=\")'      # limg means it's a small image
    imglist = re.findall(re2, html)
    return imglist

def getImgList(url = defaultUrl):
    urlDictList = mySpider.getImg(url)
    
    storageUrl = 'http://6.evandjango.sinaapp.com/storage'
    data =  {'urlDictList': urlDictList}
    encodeData = urllib.urlencode(data)
    req = urllib2.Request(storageUrl, encodeData)
    response = urllib2.urlopen(req)
    
    return urlDictList
