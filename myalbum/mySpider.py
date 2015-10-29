# -*- coding: utf-8 -*-
'''
my own spider
'''
import urllib
import urllib2
import re
import doctest
import os
import pdb

class urlInfo():
    # store the info of image
    def __init__(self, href = r'http://evandjango.sinaapp.com', src = '', description = r'evan'):
        self.href = href
        self.src = src
        self.description = description

    def show(self):
        print self.href, self.description, self.src
        
def getImg(url = r'http://www.meizitu.com'):
    htmlFile = getHtml(url)
    urlInfoList = []
    
    reg = r'<a.+?href="(.+?)".+?title="(.+?)".+?src="(.+?\.jpg.*?)"' # if has 3 properties
    imgre = re.compile(reg)
    imglist = re.findall(imgre, htmlFile)

    if imglist == []:
        reg = r'<a.+?href="(.+?)"[\S|\s]*?src="(.+?\.jpg.*?)"'  # if has 2 properties
        imgre = re.compile(reg)
        imglist = re.findall(imgre, htmlFile)
        
        if imglist == []:
            reg = r'src="(.+?jpg.*?)"'  # if only has one property
            imgre = re.compile(reg)
            imglist = re.findall(imgre, htmlFile)

    for i in imglist:
##        pdb.set_trace()
        if len(i) == 3:
            temp = urlInfo(i[0], i[2], i[1])    # care for the order
        elif len(i) == 2:
            temp = urlInfo(i[0], i[1])
        else:
            temp = urlInfo(r'http://evandjango.sinaapp.com', i[0])
        urlInfoList.append(temp)
##        temp.show()
    return urlInfoList

def getCharset(htmlFile):
    '''
    example
    >>> print getCharset(htmlFile)
    gbk
    '''
    regCharset = r'charset="(.+?)"'     # don't know how to get charset exactly after <head>
    reCharset = re.compile(regCharset)
    charset = re.findall(reCharset, htmlFile)
    if charset  != []:
        if 'gb' in charset[0]:
            return 'gbk'
        elif 'utf-8' in charset[0]:
            return 'utf-8'
    else:
        return 'utf-8'      # set utf-8 as default choice

def urlClean(url):
    '''
    add 'http://' and 'www.'
    '''
    
    if 'www' not in url:
        if 'http' not in url:
            url = 'www.' + url
            url = 'http://' + url
        
            
            
    return url

def getHtml(url = 'http://image.baidu.com'):
    url = urlClean(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
        }
    req = urllib2.Request(url, headers = headers)
    data = urllib2.urlopen(req).read()
    charset = getCharset(data)
    # don't know why it needn't to be decoded sometimes- -
    
    try:
        data = data.decode(charset)
    except:
        print 'decode error'
    return data
    
if __name__ == "__main__":
    f = open('C:\users\evann\desktop\meizituHtml.txt', 'r')
    htmlFile = f.read()
    getImg('tuchong.com')
##    doctest.testmod(verbose = True)
    f.close()
