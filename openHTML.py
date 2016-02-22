#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib2
import sys
import re
import getip
from random import choice
reload(sys)
sys.setdefaultencoding('utf-8')

def getData(ip):
    proxyDict = {'http': ip}
    opener = urllib2.build_opener(urllib2.ProxyHandler(proxyDict))
    urllib2.install_opener(opener)
    url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
    data = urllib2.urlopen(url, None, 9).read()
    return data

def main():
    iplist = getip.getproxy()
    data = ''
    while len(iplist) > 0:
        ip = choice(iplist)
        try:
            data = getData(ip)
            break
        except:
            iplist.remove(ip)
        print 'ip:%s, proxy error, try another ip' % (ip)
    restr = r'gap-right.+?(\d+?\.\d+?\.\d+?\.\d+?)</span>'
    reg = re.compile(restr)
    result = re.findall(reg, data)
    print result
    if ip.split(':')[0] == result[0]:
        print 'proxy ok'

if __name__ == '__main__':
    main()
