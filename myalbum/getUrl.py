# -*- coding: utf-8 -*-
'''
This file connects the spider and the view, and
change class to dict or list.
This is unnecessary when 'mySpider.py' was changed to
return a list of Dict.
----
Use this again to connect to storage and keep server files seperated
----
2016-3-28
Don't store infomation to sql or storage, and use original url directly.
This file seems unnecessary now, just leave it waitting for other use.
'''
import mySpider


def getImgList(url):
    try:
        urlDictList = mySpider.getImg(url)
    except:
        urlDictList = [{'href': 'evandjango.sinaapp.com',
                        'src': '/static/images/noImage.jpg',
                        'description': 'no description'}]
    fixed_site = mySpider.urlClean(url)
    return fixed_site, urlDictList
