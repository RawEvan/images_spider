import sae
import sae.storage
import urllib2
from datetime import datetime
import pdb
from myalbum.models import ImgStorage

def storeImage(imgSrc):
    data = urllib2.urlopen(imgSrc).read()
    path = imgSrc.split('/')[2] + '/'
    # if '/' in file name there will be problems
    filename = path + imgSrc.replace('/', '@')

    # save to storage
    bucket = sae.storage.Bucket('images')
    bucket.put()
    bucket.put_object(filename, data)
    stUrl = bucket.generate_url(filename)   # get url of image in the storage

    # save infomation to sql
    ImgStorage.objects.create(originalUrl = imgSrc, storageUrl = stUrl)
    return  'ok', storageUrl 
