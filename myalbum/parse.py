#!/usr/bin/env python
#coding: utf-8
 
import urllib
import urllib2
import os
import re
import sys
 
#显示下载进度
def schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
 
#获取html源码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
#下载图片
def downloadImg(html, num, foldername):
    picpath = '%s' % (foldername)       #下载到的本地目录
    if not os.path.exists(picpath):     #路径不存在时创建一个
        os.makedirs(picpath)
    target = picpath+'/%s.jpg' % num
    myItems = re.findall('<p><a href="http:\/\/www.mzitu.com/.*?" ><img src="(.*?)" alt=".*?" /></a></p>',html,re.S)
    print 'Downloading image to location: ' + target
    urllib.urlretrieve(myItems[0], target, schedule)
 
#正则匹配分页
def findPage(html):
    myItems = re.findall('<span>(\d*)</span>', html, re.S)
    return myItems.pop()
 
#正则匹配列表
def findList(html):
    myItems = re.findall('<h2><a href="http://www.mzitu.com/(\d*)" title="(.*?)" target="_blank">.*?</a></h2>', html, re.S)
    return myItems
 
#总下载
def totalDownload(modelUrl):
    listHtml5 = getHtml(modelUrl)
    listContent = findList(listHtml)
    for list in listContent:
        html = getHtml('http://www.mzitu.com/' + str(list[0]))
        totalNum = findPage(html)
        for num in range(1, int(totalNum)+1):
            if num == 1:
                url = 'http://www.mzitu.com/' + str(list[0])
                html5 = getHtml(url)
                downloadImg(html5, str(num), str(list[1]))
            else:
                url = 'http://www.mzitu.com/' + str(list[0]) + '/'+str(num)
                html5 = getHtml(url)
                downloadImg(html5, str(num), str(list[1]))
 
if __name__ == '__main__':
    listHtml = getHtml('http://www.mzitu.com/model')    #这是其中一个模块的url，可以添加不同的模块url从而达到整站爬取。
    for model in range(1, int(findPage(listHtml))+1):
        if model == 1:
            modelUrl = 'http://www.mzitu.com/model'
            totalDownload(modelUrl)
        else:
            modelUrl = 'http://www.mzitu.com/model/page/' + str(model)
            totalDownload(modelUrl)
    print "Download has finished."
