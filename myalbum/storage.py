import sae
import sae.storage
import urllib2
from datetime import datetime
import pdb
from myalbum.models import imgstorage
from sinastorage.bucket import SCSBucket
import sinastorage

# use app's storage
def storeImage_old(imgSrc):
    try:
        savedUrl = imgstorage.objects.get(original_url = imgSrc)
    except:
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
        try:
            imgstorage.objects.get_or_create(original_url = imgSrc, storage_url = stUrl)
        except:
            pass    # solve this later

# use SCS

def storeImage(imgSrc):
    sinastorage.setDefaultAppInfo('1cjfyo5kQPdnsI3cUc6W',
                                  'a3c139370a3509f269331930515729747573aa10')
    djBucket = SCSBucket('dj-images')  # not dj_images
    
    try:
        savedUrl = imgstorage.objects.get(original_url = imgSrc)
        return savedUrl
    except:
        data = urllib2.urlopen(imgSrc).read()
        path = imgSrc.split('/')[2] + '/'
        # if '/' in file name there will be problems
        filename = path + imgSrc.replace('/', '@')
        scsResponse = djBucket.put(filename, data)  # upload the file
    
        acl = {}    # Access control list
        acl[ACL.ACL_GROUP_ANONYMOUSE] = [ACL.ACL_READ]    
        stUrl = djBucket.make_url(filename)   # get url of image in the storage
        djBucket.update_acl(stUrl, acl)     # set acl for the file 
        
        # save infomation to sql
        try:
            imgstorage.objects.get_or_create(original_url = imgSrc, storage_url = stUrl)
        except:
            print 'insert into mysql error'
            pass    # solve this later

        return stUrl
