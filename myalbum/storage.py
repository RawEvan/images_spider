import sae
import sae.storage
import urllib2
from datetime import datetime
import pdb

def storeImage(imgSrc):
    data = urllib2.urlopen(imgSrc).read()
    filename = imgSrc + '.' + imgSrc.split('.')[-1]
    bucket = sae.storage.Bucket('images')
    bucket.put()
    bucket.put_object(imgSrc, data)
    storageClient.put(filename, ob)
    return  'ok', imgSrc 
