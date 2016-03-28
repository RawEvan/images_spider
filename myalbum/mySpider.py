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
import chardet
import StringIO
import gzip

defaultUrl = r'http://www.tuchong.com'

class urlInfo():
    # store the info of image
    def __init__(self, href = defaultUrl, src = '', description = r'no description'):
        self.href = href
        self.src = src
        self.description = description

    def show(self):
        print self.href, self.description, self.src
    
def getImg(url = defaultUrl):
    '''
    this is the main function
    input  : url to be parsed
    output : a list of dictions which contains the infomation of images found
             in the html
    '''
    urlInfoList = []    # a list of the class 'urlInfo'
    imgList = []    # for img has been found
    srcList = []    # store the src of images and avoid from repeating

    htmlFile = getHtml(url)     # get the source code of the html
    
    reg = r'<a.+?href="(.+?)".+?title="(.+?)".+?src="(.+?\.jpg.*?)"' # if it has 3 properties
    imgre = re.compile(reg)
    imglist = re.findall(imgre, htmlFile)

    reg2 = r'<a.+?href="(.+?)"[\S|\s]*?src="(.+?\.jpg.*?)"'  # if it has 2 properties
    imgre2 = re.compile(reg2)
    imglist += re.findall(imgre2, htmlFile)

    reg3 = r'src="(.+?jpg)"'  # if it has only one property
    imgre3 = re.compile(reg3)
    imglist += re.findall(imgre3, htmlFile)

    # simplify this later...
    for i in imglist:   # save image info to urlInfoList
        #pdb.set_trace()
        if len(i) == 3:     # if it has 3 properties
            if i[2] not in srcList:     # if not repeat
                temp = urlInfo(i[0], i[2], i[1])    # care for the order
                srcList.append(i[2])    # save the src info and avoid from repeating
            else:
                continue
        elif len(i) == 2:
            if i[1] not in srcList:
                temp = urlInfo(i[0], i[1])
                srcList.append(i[1])
            else:
                continue
        else:                       # can't use i[0] because i isn't a list in this case
            if i not in srcList:    # avoid from saving the same image
                temp = urlInfo(defaultUrl, i)
            else:
                continue
        urlInfoList.append(temp)
        
    if urlInfoList == []:   # if there is no image found
        temp = urlInfo()
        temp.src = r'/static/images/noImage.jpg'
        urlInfoList.append(temp)
        
    urlInfoList = dealwithHref(urlInfoList, url)    # do sth to the src and href

    urlInfoList = changeClassListToDictList(urlInfoList)    # change the structure

    return urlInfoList

def decompress(data):
    isGzip = data.headers.get('Content-Encoding')
    if isGzip:
        compressedData = data.read()
        stream = StringIO.StringIO(compressedData)
        data = gzip.GzipFile(fileobj = stream)
    return data

def getHtml(url = defaultUrl):
    '''
    get the source code
    '''
    url = urlClean(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
        }
    req = urllib2.Request(url, headers = headers)
    data = urllib2.urlopen(req)
    data = decompress(data).read()  # decompress if gzip used
    # time.sleep(2)   # avoid being banned
    charset = chardet.detect(data)['encoding']
    htmlCode = data.decode(charset)
    return htmlCode

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

        # if the href head to server resource, need to be imporoved
        if urlInfo.href[0] == '/':
            urlInfo.href = url + urlInfo.href

        if '.com' not in urlInfo.href:
            splitUrl = url.split('/')[0:-1]
            baseUrl = u''.join(str + u'/' for str in splitUrl)
            urlInfo.href = baseUrl + urlInfo.href
            
    return urlInfoList

def urlClean(url):
    '''
    add 'http://' and 'www.'
    '''
    if url[0] != r'/':  # when it's internet resource
        if 'http' not in url:
            url = 'http://' + url
    elif 'localhost' in url:    #  # specially for localhost
        url = 'http://' + url
                
    else:   # when it's on the server
        pass    # need more time
    return url

def changeClassListToDictList(urlInfoList):
    '''
    change the list of class 'urlInfo' to a list of urlDict
    each urlDict contain key 'href' 'src' and 'description'
    this is a sample of urlDictList:
    urlDictList = [{'src': xxx, 'href': xxx, 'description': xxx},
                   {'src': xxx, 'href': xxx, 'description': xxx}]
    '''
    urlDictList = []
    #urlTemp = {}
  
    for eachUrlInfo in urlInfoList:
        urlTemp = {}
        urlTemp['description'] = eachUrlInfo.description
        urlTemp['href'] = eachUrlInfo.href
        urlTemp['src'] = eachUrlInfo.src
        urlDictList.append(urlTemp)
        
    return urlDictList

if __name__ == "__main__":
    # test
    htmlFile = ('/local/html/file')
    f = open(htmlFile, 'r')     # local html
    htmlFile = f.read()
    getImg('image.baidu.com')
    #doctest.testmod(verbose = True)
    f.close()
