#!/usr/bin/python
#-*-coding:utf-8-*-

from HTMLParser import HTMLParser
import urllib2
import urllib
import re
import json
import pdb
import time

defaultUrl = 'http://www.xicidaili.com'

def getHtml(url = defaultUrl):
    '''headers = {"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
            Accept-Encoding:gzip, deflate, sdch
            Accept-Language:zh-CN,zh;q=0.8
            Cache-Control:max-age=0
            Connection:keep-alive
            Host:www.xicidaili.com
            Upgrade-Insecure-Requests:1
            User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36)"}
            '''
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36)"}
    req = urllib2.Request(url = url, headers = headers)
    data = urllib2.urlopen(req)
    return data.read()

def getproxy(url = defaultUrl):
    f = open("IPInfo.txt", 'rb')
    try:
        IPFile = json.loads(f.read())
        if time.time() - IPFile['time'] < 180 and IPFile['IPList']:
            print '----ip list don\'t need update----'
            return IPFile['IPList'] 
    except:
        pass
    finally:
        f.close()

    #iplist is out-of-date, update it
    print '----update ip list-------'
    IPList = []
    try:
        data = getHtml()
    except:
        print 'urlopen error:%s' % (url)
    reg = r'<tr class="odd">[\s\S]*?<td>(\d+?\.\d+?\.\d+?\.\d+?)</td>[\s\S]*?<td>(.+?)</td>'
    regcompl = re.compile(reg)
    iplist = re.findall(regcompl, data)
    for IP, port in iplist:
        newIP = str(IP) + ':' +str(port) 
        IPList.append(newIP)
    saveIP(IPList)
    return IPList

def saveIP(IPList = ['127.0.0.0:80']):
    fileDict = {}
    fileDict['IPList'] = IPList
    fileDict['time'] = time.time()
    fileDict['ctime'] = time.ctime()
    string = json.dumps(fileDict)
    f = open('IPInfo.txt', 'wb')
    try:
        f.write(string)
    finally:
        f.close()
    print 'time:', time.localtime()

def main():
    getproxy()
if __name__ == "__main__":
    #getproxy()
    #saveIP()
    main()
