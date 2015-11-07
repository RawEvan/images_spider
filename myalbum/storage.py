import sae
import sae.storage
import urllib2
from datetime import datetime
import pdb

def storeImage(imgSrc):
    data = urllib2.urlopen(imgSrc).read()
    filename = imgSrc.replace('/', '@') + '.' + imgSrc.split('.')[-1]
    bucket = sae.storage.Bucket('images')
    bucket.put()
    bucket.put_object(filename, data)
    return  'ok', imgSrc 
