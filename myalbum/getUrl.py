# -*- coding: utf-8 -*-
'''
this file connects the spider and the view
'''
import re
import urllib2
import mySpider

defaultUrl = 'image.baidu.com'

def getHtml(url):   # old function 
    html = ''
    try:
        html = urllib2.urlopen(url).read().decode('gbk')# try to use gbk
    except:
        pass
    try:
        html = urllib2.urlopen(url).read().decode('utf-8')# try to use utf-8
    except:
        pass
    if html == '':
        html = '/static/images/noImage.jpg'
    return html

def getImgList_old(url = defaultUrl):   # old function
    html = getHtml(url)
##    re2=r'meizitu.com/.+\.jpg'
    re2 = '(?<=src=\").+?(?<!limg)\.jpg(?=\")'      # limg means it's a small image
    imglist = re.findall(re2, html)
    return imglist

def getImgList(url = defaultUrl):
    imgInfoList = mySpider.getImg(url)
    imgSrcList = []     # don't use this now
    imgHrefList = []    # don't use this now
    srcHrefDict = {}
    for imgInfo in imgInfoList:
        srcHrefDict[imgInfo.src] = imgInfo.href
    return srcHrefDict
