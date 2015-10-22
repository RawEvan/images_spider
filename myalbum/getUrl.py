import parse_tuchong as pt
import re

def getImgList(url = "http://www.tuchong.com"):
    html = pt.getHtml(url)
##    re2=r'meizitu.com/.+\.jpg'
    re2 = '(?<=src=\").+?(?<!limg)\.jpg(?=\")'
    imglist = re.findall(re2, html)
    return imglist

##print getImgList()
