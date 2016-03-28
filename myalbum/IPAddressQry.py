#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib2
import sys
import re
import getProxy
from random import choice
reload(sys)
sys.setdefaultencoding('utf-8')

def getData(ip):
    proxyDict = {'http': ip}
    opener = urllib2.build_opener(urllib2.ProxyHandler(proxyDict))
    urllib2.install_opener(opener)
    url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
    header = {'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3','User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}
    req = urllib2.Request(url, headers = header)
    data = urllib2.urlopen(req, None, 9).read()
    return data

def testProxy():
    IPList = getProxy.getProxy()
    data = ''
    while len(IPList) > 0:
        ip = choice(IPList)
        try:
            data = getData(ip)
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

def main():
    testProxy()

if __name__ == '__main__':
    main()
