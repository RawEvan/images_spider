#!/usr/bin/python
#coding:utf-8
import json
dic = {}
dic["ip"] = '111'
jsonDic = json.dumps(dic)
f = open('file.txt','wb')
f.write(jsonDic)
f.close()
