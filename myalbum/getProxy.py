#!/usr/bin/python
# -*-coding:utf-8-*-

import urllib2
import urllib
import re
import json
import time
import sys
import logging
from random import choice
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')


DEFAULT_URL = 'http://www.xicidaili.com'
LOG_FILE = 'proxy.log'

def IPQueryHTML(ip):
    proxyDict = {'http': ip}
    opener = urllib2.build_opener(urllib2.ProxyHandler(proxyDict))
    urllib2.install_opener(opener)
    url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
    header = {'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
              'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}
    req = urllib2.Request(url, headers=header)
    data = urllib2.urlopen(req, None, 9).read()
    return data


def testProxy():
    IPList = getProxy.getProxy()
    data = ''
    while len(IPList) > 0:
        ip = choice(IPList)
        try:
            data = IPQueryHTML(ip)
            break
        except:
            IPList.remove(ip)
        print 'ip:%s, proxy error, try another ip' % (ip)
    getProxy.saveIP(IPList)
    restr = r'gap-right.+?(\d+?\.\d+?\.\d+?\.\d+?)</span>'
    reg = re.compile(restr)
    result = re.findall(reg, data)
    print result
    if ip.split(':')[0] == result[0]:
        print 'proxy ok'


def getHtml(url=DEFAULT_URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36)"}
    req = urllib2.Request(url=url, headers=headers)
    data = urllib2.urlopen(req)
    return data.read()


def getProxy(url=DEFAULT_URL):
    try:
        f = open("IPInfo.txt", 'rb')
        IPFile = json.loads(f.read())
        if time.time() - IPFile['time'] < 180 and IPFile['IPList']:
            print '----ip list don\'t need update----'
            return IPFile['IPList']
    except:
        print 'failed to open IPInfo.txt'
    finally:
        f.close()

    # IPList is out-of-date, update it
    print '----update ip list-------'
    IPList = []
    try:
        data = getHtml()
    except:
        print 'urlopen error:%s' % (url)
    reg = r'<tr class="odd">[\s\S]*?<td>(\d+?\.\d+?\.\d+?\.\d+?)</td>[\s\S]*?<td>(.+?)</td>'
    regcompl = re.compile(reg)
    result = re.findall(regcompl, data)
    for IP, port in result:
        newIP = str(IP) + ':' + str(port)
        IPList.append(newIP)
    try:
        saveIP(IPList)
    except:
        print 'failed to save ip to IPIndo.txt'
    return IPList


def saveIP(IPList=['127.0.0.0:80']):
    if not IPList:
        getProxy()
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
    getProxy()

if __name__ == "__main__":
    # getProxy()
    # saveIP()
    main()
