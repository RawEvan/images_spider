# -*- coding: utf-8 -*-
'''
this file connects the spider and the view
'''
import re
import urllib2
import mySpider

defaultUrl = 'www.meizitu.com'

def getHtml(url):   # old function 
    html = ''
    try:
        html = urllib2.urlopen(url).read().decode('gbk')#解码为gbk
    except:
        pass
    try:
        html = urllib2.urlopen(url).read().decode('utf-8')#解码为utf-8
    except:
        pass
    if html == '':
        html = '/static/images/404-luotianyi.jpg'
    return html

def getImgList_old(url = defaultUrl):
    html = getHtml(url)
##    re2=r'meizitu.com/.+\.jpg'
    re2 = '(?<=src=\").+?(?<!limg)\.jpg(?=\")'      # limg ??
    imglist = re.findall(re2, html)
    return imglist

def getImgList(url = defaultUrl):
    imgInfoList = mySpider.getImg(url)
    imgSrcList = []
    imgHrefList = []
    srcHrefDict = {}
    for imgInfo in imgInfoList:
        imgSrcList.append(imgInfo.src)
        imgHrefList.append(imgInfo.href)
        srcHrefDict[imgInfo.src] = imgInfo.href
    return srcHrefDict
