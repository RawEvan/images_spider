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
    for imgInfo in urlDictList:
        storage.storeImage(imgInfo['src'])
    return urlDictList
