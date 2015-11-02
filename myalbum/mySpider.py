# -*- coding: utf-8 -*-
'''
introduce :a simple spider to get infomation of images
           and store these to the class named urlInfo
author: LiAiWen
e-mail: 909798432@qq.com
'''
import urllib
import urllib2
import re
import doctest
import os
import pdb
import time

defaultUrl = r'image.baidu.com'

class urlInfo():
    # store the info of image
    def __init__(self, href = defaultUrl, src = '', description = r'evan'):
        self.href = href
        self.src = src
        self.description = description

    def show(self):
        print self.href, self.description, self.src
        
def getImg(url = defaultUrl):
    htmlFile = getHtml(url)
    urlInfoList = []
    imgList = []    # for img has been find
    
    reg = r'<a.+?href="(.+?)".+?title="(.+?)".+?src="(.+?\.jpg.*?)"' # if it has 3 properties
    imgre = re.compile(reg)
    imglist = re.findall(imgre, htmlFile)

    reg2 = r'<a.+?href="(.+?)"[\S|\s]*?src="(.+?\.jpg.*?)"'  # if it has 2 properties
    imgre2 = re.compile(reg2)
    imglist += re.findall(imgre2, htmlFile)

    reg3 = r'src="(.+?jpg)"'  # if it has only one property
    imgre3 = re.compile(reg3)
    imglist += re.findall(imgre3, htmlFile)

    for i in imglist:   # save image info to urlInfoList
        #pdb.set_trace()
        if len(i) == 3:     # if it has 3 properties
            temp = urlInfo(i[0], i[2], i[1])    # care for the order
            imgList.append(i[2])    # save the image info
        elif len(i) == 2:
            temp = urlInfo(i[0], i[1])
            imgList.append(i[1])
        else:   # can't use i[0] because i isn't a list in this case
            if i not in imgList:    # avoid from saving the same image
                temp = urlInfo(defaultUrl, i)
        urlInfoList.append(temp)
        
    if urlInfoList == []:   # if there is no image found
        temp = urlInfo()
        temp.src = r'/static/images/noImage.jpg'
        urlInfoList.append(temp)
        
    urlInfoList = dealwithHref(urlInfoList, url)
        
    return urlInfoList


def dealwithHref(urlInfoList, url):
    '''
    if urlInfoList == []:   # if there is no image found
        temp = urlInfo()    # why it says 'the urlInfo referenced before assignment'
                            # but this can work in function getImg() below
        urlInfoList.append(temp)
    '''
    for urlInfo in urlInfoList:
        # specially for localhost, change './xxx' to '/../xxx'
        if urlInfo.src[0] == r'.':
            urlInfo.src = 'http://localhost:9000/' + urlInfo.src
            
        if urlInfo.href == r'#':
            urlInfo.href = '/static/images/noImage.jpg'
            
        if urlInfo.href[0] == '/':  # if the href head to server resource
            urlInfo.href = url + urlInfo.href
            
        
            
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
    if url[0] != r'/':  # when it's internet resource
        if 'http' not in url:
            url = 'http://' + url
                
    else:   # when it's on the server
        pass    # need more time
    return url

def getHtml(url = defaultUrl):
    url = urlClean(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
        }
    req = urllib2.Request(url, headers = headers)
    data = urllib2.urlopen(req).read()
    time.sleep(2)   # avoid being banned
    charset = getCharset(data)
    # don't know why it needn't to be decoded sometimes- -
    try:
        data = data.decode(charset)
    except:
        print 'decode error'
        pass    # need more time
    return data
    
if __name__ == "__main__":
    # test
    f = open('C:\users\evann\desktop\meizituHtml.html', 'r')     # local html
    htmlFile = f.read()
    getImg('image.baidu.com')
    #doctest.testmod(verbose = True)
    f.close()
