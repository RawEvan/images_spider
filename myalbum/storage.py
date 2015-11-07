import sae
import sae.storage
import urllib2
from datetime import datetime
import pdb

def storeImage(imgSrc):
    data = urllib2.urlopen(imgSrc).read()
    path = imgSrc.split('/')[2] + '/'
    # if '/' in file name there will be problems
    filename = path + imgSrc.replace('/', '@')  
    bucket = sae.storage.Bucket('images')
    bucket.put()
    bucket.put_object(filename, data)
    return  'ok', imgSrc 
